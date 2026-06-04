import gradio as gr
from query import ask

def handle_query(question):
    if not question.strip():
        return "Please input a valid question.", "No sources retrieved."
        
    result = ask(question)
    
    if not result["sources"]:
        source_display = "No sources utilized (Out of scope or insufficient text data)."
    else:
        source_display = "\n".join(f"• {s}" for s in result["sources"])
        
    return result["answer"], source_display

# Build interface according to the course layout template specification
with gr.Blocks(title="The Unofficial Guide: Purdue CS240") as demo:
    gr.Markdown("# 🎓 The Unofficial Guide: Purdue CS240 / Turkstra")
    gr.Markdown("Ask plain-language questions regarding grading policies, AI scanners, and course feedback.")
    
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(label="Your question", placeholder="e.g., How does the tracking tool commit files?", lines=2)
            btn = gr.Button("Ask System", variant="primary")
        
        with gr.Column():
            answer = gr.Textbox(label="Answer", lines=8, interactive=False)
            sources = gr.Textbox(label="Retrieved from", lines=4, interactive=False)
            
    # Establish execution trigger paths
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch()