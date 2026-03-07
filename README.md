# 💎 Graphene Prism
**A Prompt Orchestration Engine**

Graphene Prism is a local RAG-powered prompt editor designed for high-precision prompt engineering. Built with **PyQt6**, **LangChain**, and **Ollama**, it leverages local LLMs to transform vague intents into structured, high-fidelity master prompts.

## 🚀 Key Features
* **Semantic Retrieval:** Uses `mxbai-embed-large` to pull engineering principles from your PDF library.
* **Interactive UI:** Custom `QTextCursor` logic for tabbing through `[placeholders]`.
* **Local-First:** Privacy-focused inference using `Llama 3.2` via Ollama.
* **Modular Architecture:** Designed for future **MCP (Model Context Protocol)** integration.

## 🛠️ Setup
1. `ollama pull llama3.2:3b`
2. `ollama pull mxbai-embed-large:335m`
3. `pip install -r requirements.txt`
4. Place PDFs in `/resources` and run `python main.py`.
