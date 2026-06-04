import os
import re
import pdfplumber

def load_documents(docs_dir="documents"):
    """
    Milestone 3: Stage 1 - Document Ingestion
    Loads text from .txt, .md, and digitally created .pdf files in the documents folder.
    """
    raw_documents = []
    
    # Verify directory exists
    if not os.path.exists(docs_dir):
        print(f"Error: Directory '{docs_dir}' not found.")
        return raw_documents

    for filename in os.listdir(docs_dir):
        file_path = os.path.join(docs_dir, filename)
        
        # Skip directories or gitkeep files
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue
            
        text = ""
        try:
            if filename.endswith('.pdf'):
                # Extract using pdfplumber as instructed in the project guide
                with pdfplumber.open(file_path) as pdf:
                    text = "\n\n".join(p.extract_text() for p in pdf.pages if p.extract_text())
            elif filename.endswith(('.txt', '.md')):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            else:
                print(f"Skipping unsupported file type: {filename}")
                continue
                
            if text.strip():
                raw_documents.append({"source": filename, "text": text})
                print(f"Successfully loaded: {filename} ({len(text)} characters)")
            else:
                print(f"Warning: {filename} resulted in empty text. (Check for OCR/Scanned images)")
                
        except Exception as e:
            print(f"Failed to read {filename}: {str(e)}")
            
    return raw_documents

def clean_text(text):
    """
    Milestone 3: Stage 2 - Text Cleaning
    Removes HTML artifacts, markdown link wrappers, upvote indicators, 
    and systemic noise while preserving the raw student insight.
    """
    # 1. Clear common HTML formatting leftover noise
    text = re.sub(r'&\w+;', ' ', text)
    
    # 2. Clear out repetitive Rate My Professor specific noise (e.g., Helpful 0 4, Quality, Difficulty indicators)
    text = re.sub(r'Helpful\s*\d+\s*\d*', '', text)
    text = re.sub(r'QUALITY\s*CS\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'DIFFICULTY\s*\d+\.\d+', '', text)
    
    # 3. Strip down ugly Reddit link / voter visual formatting clutter
    text = re.sub(r'&#x21C5;\s*\d+', '', text) # Strips upvote arrows from script data
    text = re.sub(r'\[Visit\]\(https?://[^\)]+\)', '', text)
    text = re.sub(r'!\[gif\]\([^\)]+\)', '', text)
    text = re.sub(r'!\[preview\]\([^\)]+\)', '', text)
    
    # 4. Standardize whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Strip common Reddit AutoModerator greeting banners
    text = re.sub(r'Looking for information on specific courses or professors\?.*?(Transfer Credit Course Equivalency Guide|talk to your advisor as well!)', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    return text.strip()

def split_into_chunks(cleaned_docs, chunk_size=500, overlap=100):
    """
    Milestone 3: Stage 3 - Chunking Strategy
    Implements a recursive-character baseline split using specified parameters.
    """
    all_chunks = []
    
    for doc in cleaned_docs:
        text = doc["text"]
        source_name = doc["source"]
        
        start = 0
        chunk_index = 0
        text_length = len(text)
        
        # Guard rail for exceptionally short inputs
        if text_length <= chunk_size:
            all_chunks.append({
                "text": text,
                "metadata": {"source": source_name, "chunk_id": f"{source_name}_0"}
            })
            continue
            
        while start < text_length:
            end = start + chunk_size
            chunk_text = text[start:end]
            
            # Try to snap backwards cleanly to the end of a sentence or boundary if possible
            if end < text_length:
                # Find the last space or period in the terminal section to keep words unbroken
                boundary = max(chunk_text.rfind('. '), chunk_text.rfind('\n'), chunk_text.rfind(' '))
                if boundary > chunk_size // 2: # Don't snap back too far
                    end = start + boundary + 1
                    chunk_text = text[start:end]
            
            all_chunks.append({
                "text": chunk_text.strip(),
                "metadata": {"source": source_name, "chunk_id": f"{source_name}_{chunk_index}"}
            })
            
            chunk_index += 1
            start += (end - start) - overlap # Progress forward minus the overlap region
            
    return all_chunks

if __name__ == "__main__":
    print("\n=========================================================")
    print("--- Starting Milestone 3 Document Ingestion Pipeline ---")
    print("=========================================================")
    
    # Check current workspace architecture
    current_dir = os.getcwd()
    target_docs_folder = os.path.join(current_dir, "documents")
    
    print(f"[*] Executing from tracking directory: {current_dir}")
    print(f"[*] Scanning for folder at: {target_docs_folder}")
    print(f"[*] Directory existence check: {os.path.exists(target_docs_folder)}")
    
    if os.path.exists(target_docs_folder):
        contents = os.listdir(target_docs_folder)
        print(f"[*] Explicit inventory of files discovered: {contents}")
    else:
        print("[!] ERROR: The 'documents/' directory does not exist at this path location.")
    print("---------------------------------------------------------\n")

    # 1. Run Ingestion Execution
    raw_data = load_documents("documents")
    print(f"\n[*] Pipeline Ingestion Step Complete. Raw Files Loaded: {len(raw_data)}")
    
    if not raw_data:
        print("[!] STOPPING PIPELINE: No text data gathered. Ensure your .md, .txt, and .pdf files are inside the 'documents/' folder.")
        exit()

    # 2. Clean Text
    print("[*] Processing Text Cleaning Patterns...")
    cleaned_data = []
    for doc in raw_data:
        cleaned_text_content = clean_text(doc["text"])
        cleaned_data.append({"source": doc["source"], "text": cleaned_text_content})
        
    # 3. Apply Chunking Strategy
    print("[*] Slicing Content into Semantically Guarded Chunks...")
    processed_chunks = split_into_chunks(cleaned_data)
    print(f"[✓] SUCCESS: Total Database Chunks Formed: {len(processed_chunks)}\n")
    
    # 4. Mandatory Inspection Checkpoint Verification
    print("--- Milestone Checkpoint Validation: Inspecting 5 Random Chunks ---\n")
    import random
    sample_chunks = random.sample(processed_chunks, min(len(processed_chunks), 5))
    
    for idx, chunk in enumerate(sample_chunks, 1):
        print(f"=== SAMPLE CHUNK {idx} ===")
        print(f"Source Document: {chunk['metadata']['source']}")
        print(f"ID Field: {chunk['metadata']['chunk_id']}")
        print(f"Character Count: {len(chunk['text'])}")
        print(f"Content Preview:\n{chunk['text']}\n")
        print("-" * 40)