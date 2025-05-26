import os
from dotenv import load_dotenv

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
COSMOS_DATABASE = os.getenv("COSMOS_DATABASE", "chatbotdb")
COSMOS_CONTAINER = os.getenv("COSMOS_CONTAINER", "conversations")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
