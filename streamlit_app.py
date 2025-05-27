from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env at project start

import streamlit as st
import uuid
from app.db import CosmosDB
from app.chatbot import Llama3Chatbot

st.set_page_config(page_title="Llama3 Chatbot", page_icon="🤖")

# Generate or get session ID for each user
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Initialize Cosmos DB and chatbot
db = CosmosDB()
bot = Llama3Chatbot(st.session_state.session_id, db)

st.title("🤖 Llama3 Chatbot")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = db.get_conversation(st.session_state.session_id)

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(message)

# Chat input
if prompt := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    response = bot.chat(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    # Update session state and CosmosDB
    st.session_state.chat_history.append(("user", prompt))
    st.session_state.chat_history.append(("assistant", response))
