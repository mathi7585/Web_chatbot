import gradio as gr
from web_search import web_search
from llm import generate_answer

def chatbot(query):
    web_context = web_search(query)
    answer = generate_answer(query, web_context)
    return answer

gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Ask anything..."),
    outputs=gr.Textbox(lines=10),
    title="🌐 Web Search AI Chatbot",
    description="Answers questions using live web search + LLM"
).launch()
