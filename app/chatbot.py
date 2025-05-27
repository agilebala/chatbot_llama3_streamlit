from langchain_ollama import OllamaLLM
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from .config import OLLAMA_MODEL

class Llama3Chatbot:
    def __init__(self, session_id, db):
        self.llm = OllamaLLM(model=OLLAMA_MODEL)
        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(llm=self.llm, memory=self.memory)
        self.db = db
        self.session_id = session_id

        # Load previous conversation into memory
        for role, message in self.db.get_conversation(session_id):
            if role == "user":
                self.memory.chat_memory.add_user_message(message)
            else:
                self.memory.chat_memory.add_ai_message(message)

    def chat(self, user_input):
        self.db.save_message(self.session_id, "user", user_input)
        response = self.chain.run(user_input)
        self.db.save_message(self.session_id, "ai", response)
        return response

