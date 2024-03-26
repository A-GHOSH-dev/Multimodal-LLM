import os

import streamlit as st
from decouple import config

from langchain.llms import OpenAI

from langchain.chains import RetrievalQA
# from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

import chromadb
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


st.set_page_config(page_title="Chat With YT", layout="centered")
st.title("Chat With YouTube Video")

# set API key
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

persistent_client = chromadb.PersistentClient(path="./vector_store_003")

# embedding function
embedding_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma(
    embedding_function=embedding_function,
    persist_directory="./vector_store_003",
    collection_name="google_cloud"
)

prompt = PromptTemplate(
    template="""Given the context of about a video. Answer the user in a friendly and precise manner.
    
    Context: {context}
    
    Human: {question}
    
    AI:""",
    input_variables=["context", "question"]
)

# set initial message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there, how can I help you"}
    ]

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(
        temperature=0.6
    ),
    chain_type="stuff",
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={
        "prompt": prompt
    }
)

# display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# get user input
user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = qa_chain(
                {"query": user_prompt}
            )
            st.write(ai_response["result"])

            for doc in ai_response["source_documents"]:
                st.write(doc)

    new_ai_message = {"role": "user", "content": ai_response}
    st.session_state.messages.append(new_ai_message)
