# 🤖 Chatbot

Chatbot is an intelligent AI assistant that answers user queries by leveraging real-time web search results and advanced language models. It provides reliable information, and gracefully handles cases where no information is found.

---
## 🚀 Introduction

Chatbot combines the power of web search and Large Language Models (LLMs) to deliver accurate answers to user questions. By searching the web and using a smart prompt, it ensures up-to-date and relevant responses. The application is built using Python and Gradio for an intuitive web interface.

---

## ✨ Features

- 🔍 **Web Search Integration**: Finds updated information using Tavily web search.
- 🤖 **AI-Powered Responses**: Generates answers with OpenRouter-powered LLMs.
- 🛡️ **Reliable Results**: Clearly indicates when information is not available.
- 🖥️ **Simple UI**: Gradio-based interface for easy interaction.
- 🧩 **Modular Codebase**: Clean separation of search, prompt, and AI logic.

---

## ⚡ Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/mathi7585/Chatbot.git
    cd Chatbot
    ```

2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set API keys**
    - Create a `.env` file in the project root:
      ```
      OPENROUTER_API_KEY=your_openrouter_api_key
      TAVILY_API_KEY=your_tavily_api_key
      ```
    - Get your API keys from [OpenRouter](https://openrouter.ai/) and [Tavily](https://www.tavily.com/).

---

## 🛠️ Usage

1. **Run the application**
    ```bash
    python app.py
    ```

2. **Interact via Gradio web interface**
    - Open the URL shown in your terminal (typically [http://localhost:7860](http://localhost:7860)).
    - Type your question and receive AI-powered answers based on web search results.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📂 Project Structure

```text
├── app.py           # Main Gradio interface
├── llm.py           # LLM answer generation logic
├── prompts.py       # System prompt for AI
├── web_search.py    # Web search integration
├── requirements.txt # Python dependencies
├── .env.example     # Example environment variables
└── README.md        # Project documentation
```

---

> **Made with ❤️ using OpenRouter, Tavily, and Gradio**


## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/mathi7585/Chatbot
