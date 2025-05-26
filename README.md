# Llama 3 Chatbot with Cosmos DB

A Python chatbot using Ollama Llama 3 (LangChain) and Azure Cosmos DB for chat history persistence.

## Features

- Local Llama 3 inference (via Ollama)
- Chat history stored in Cosmos DB (partitioned by session)
- Easy environment configuration
- Modular, extensible, and production-friendly

## Usage

1. Fill `.env` with your Cosmos DB credentials and model name.
2. Start Ollama and pull the model: `ollama pull llama3`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`
