import os
import streamlit as st 
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
#above lines import necessary classes and all

st.title("Daarsiel's first AI chatbot") #big title ahh
if "messages" not in st.session_state:
    st.session_state.messages=[]
#above if block checks for session state messages and if there aren't any, it initialises as it should
#basically a way to initialise at the start

client= Groq(api_key=os.environ.get("GROQ_API_KEY")) #API key gotta hide it
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#above block is basically a renderer for the chatbot

if prompt:= st.chat_input("Prompt... "):
    with st.chat_message("user"): #rendering using streamlit
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt}) #saves the message history for context
    completion=client.chat.completions.create( #finally calling the AI for the response
    model="llama-3.3-70b-versatile", 
    messages=st.session_state.messages
    )
    response=completion.choices[0].message.content #storing the FIRST response from the AI
    with st.chat_message("assistant"):
        st.markdown(response) #and then returning it after rendering it through an assistant
    st.session_state.messages.append({"role":"assistant", "content":response}) #saves the message as the script reruns

#anyways I still need to throughly learn streamlit goddamn
