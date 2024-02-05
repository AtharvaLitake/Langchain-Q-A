#Q&A Chatbot
import os
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv() #take environement variables from .env

#importing streamlit for frontend
import streamlit as st

#function to load openai model and get respone

def getresponse(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.6)
    response=llm(question)
    return response

#initializing streamlit

st.set_page_config(page_title="Q&A - Nice Internship")
st.header("LANGCHAIN LEARNINGS")
#fetching input
input=st.text_input("Input: ",key="input")
response=getresponse(input)

submit=st.button("Ask a Question")
#if submitted

if submit:
    st.subheader("The Response is")
    st.write(response)

