import os
import webbrowser
import streamlit as st
import pickle
import time
import faiss
from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
# from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
# from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
# from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)
flask_app_url_1 = "http://127.0.0.1:2500"
flask_app_url_2 = "http://127.0.0.1:8502"
flask_app_url_3 = "http://127.0.0.1:2700"
flask_app_url_4 = "http://127.0.0.1:2701"
flask_app_url_5 = "http://127.0.0.1:8503"


st.title("QueryMintAI: Equity Research Analysis ChatBot 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

# file_path = "faiss_store_openai.pkl"
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9, max_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data - original data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )

    # text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, 
    #                                       chunk_overlap=200, length_function=len)
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # my changes to remove error
    
    #print(docs)
    # docs = text_splitter.split_text(data)
    
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    #correcting the index error: zipping
    # text_embeddings = zip(docs, embeddings)
    #print('########################################################################################')
    #instead of from_documents use embeddingss
    #print(embeddings)
    # print('########################################################################################')
    # print(text_embeddings)
    # if text_embeddings:
    #     index = faiss.IndexFlatL2(len(text_embeddings[0]))
    # else:
    #     print("Text embeddings list is empty.")


    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    

    # vectorstore_openai = FAISS.from_texts(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)
    #vectorstore_openai.save_local("faiss_store")
    
    
    
query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
    # if FAISS.load_local("faiss_store", OpenAIEmbeddings()):
        with open(file_path, "rb") as f:
             vectorstore = pickle.load(f)
        # vectorstore=FAISS.load_local("faiss_store", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        # vectorstore=FAISS.load_local("faiss_store", OpenAIEmbeddings())
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
        st.header("Answer")
        st.write(result["answer"])
        # Display sources, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by newline
            for source in sources_list:
                st.write(source)
                
    
# query = main_placeholder.text_input("Question: ")
# if query:
#     # if os.path.exists(file_path):
#     if FAISS.load_local("faiss_store", OpenAIEmbeddings()):
#         # with open(file_path, "rb") as f:
#         #     vectorstore = pickle.load(f)
#         # vectorstore=FAISS.load_local("faiss_store", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
#         vectorstore=FAISS.load_local("faiss_store", OpenAIEmbeddings())
#         chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
#         result = chain({"question": query}, return_only_outputs=True)
#         # result will be a dictionary of this format --> {"answer": "", "sources": [] }
#         st.header("Answer")
#         st.write(result["answer"])
#         # Display sources, if available
#         sources = result.get("sources", "")
#         if sources:
#             st.subheader("Sources:")
#             sources_list = sources.split("\n")  # Split the sources by newline
#             for source in sources_list:
#                 st.write(source)

# Create a button
# if st.button("Chat with your Documents Bot"):
#     # When the button is clicked, open the hyperlink
#     st.markdown(f"[Chat with your Documents Bot]({flask_app_url_1})")
if st.button("Documents Bot"):
    # When the button is clicked, open the hyperlink
    webbrowser.open(flask_app_url_1)
if st.button("Databases Bot"):
    webbrowser.open(flask_app_url_2)
if st.button("Audio Bot"):
    webbrowser.open(flask_app_url_3)
    
if st.button("Image Bot"):
    webbrowser.open(flask_app_url_4)
if st.button("Video Bot"):
    webbrowser.open(flask_app_url_5)