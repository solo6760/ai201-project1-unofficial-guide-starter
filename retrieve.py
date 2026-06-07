import os
import chromadb
from chromadb.utils import embedding_functions
from ingest import load_documents, clean_text, split_into_chunks

def build_vector_store():
    print("--- Initializing Milestone 4 Vector Store Construction ---")
    
    # 1. Run the ingestion pipeline to collect text chunks
    raw_data = load_documents("documents")
    cleaned_data = [{"source": doc["source"], "text": clean_text(doc["text"])} for doc in raw_data]
    processed_chunks = split_into_chunks(cleaned_data)
    
    if not processed_chunks:
        print("[!] Error: No text chunks discovered to write into the database.")
        return None

    # 2. Configure a Persistent Local Disk Storage Path
    # Using a relative workspace folder ensures database states remain intact across sessions
    db_path = os.path.join(os.getcwd(), "chroma_db")
    chroma_client = chromadb.PersistentClient(path=db_path)
    
    # 3. Connect to the Local Embedding Model
    # Uses sentence-transformers (all-MiniLM-L6-v2) as specified in the project requirements
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # 4. Initialize the database collection (clearing out old data snapshots first)
    collection_name = "purdue_cs240_guide"
    try:
        chroma_client.delete_collection(name=collection_name)
        print("[*] Detected historical collection state. Resetting records...")
    except Exception:
        pass
        
    collection = chroma_client.create_collection(
        name=collection_name, 
        embedding_function=embedding_func
    )
    
    # 5. Restructure text lists, chunk IDs, and source links for batch upload
    documents_list = [chunk["text"] for chunk in processed_chunks]
    ids_list = [chunk["metadata"]["chunk_id"] for chunk in processed_chunks]
    metadata_list = [{"source": chunk["metadata"]["source"]} for chunk in processed_chunks]
    
    print(f"[*] Calculating vectors and tracking metadata for {len(documents_list)} chunks...")
    collection.add(
        documents=documents_list,
        metadatas=metadata_list,
        ids=ids_list
    )
    print("SUCCESS: Database records written cleanly to local disk storage.")
    return collection

def execute_semantic_search(collection, user_query, k=4):
    """
    Queries the vector database for top-k matching documents using cosine semantic distance.
    """
    print(f"\n[QUERY]: '{user_query}' (Top-k: {k})")
    print("=" * 70)
    
    results = collection.query(
        query_texts=[user_query],
        n_results=k
    )
    
    # Parse and loop structured collection outputs
    for idx in range(len(results['documents'][0])):
        chunk_text = results['documents'][0][idx]
        source_doc = results['metadatas'][0][idx]['source']
        distance_score = results['distances'][0][idx]
        chunk_id = results['ids'][0][idx]
        
        print(f"▶ MATCH {idx + 1} | Vector Distance Score: {distance_score:.4f}")
        print(f"   Source Linkage: {source_doc} [{chunk_id}]")
        print(f"   Extracted Segment:\n   {chunk_text}")
        print("-" * 70)

if __name__ == "__main__":
    # Compile and verify vector engine creation
    vector_collection = build_vector_store()
    
    if vector_collection:
        print("\n--- Running Evaluation Checkpoint Search Tests ---")
        
        # Test Query 1: Tracking algorithm policy shifts
        execute_semantic_search(vector_collection, "What did Turkstra decide about assignments before homework 11?")
        
        # Test Query 2: Tool development mechanics
        execute_semantic_search(vector_collection, "How does the tracking tool or fine grained source control commit files?")