import os

from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers.audio import OpenAIWhisperParser, OpenAIWhisperParserLocal
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

# from langchain.vectorstores import Chroma
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

from decouple import config


local = False
save_dir = "./yt_audios"


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

try:
    # get URL
    url = ["https://www.youtube.com/watch?v=wNOs3LlsH6k"]
    if local:
        loader = GenericLoader(YoutubeAudioLoader(
            urls=url,
            save_dir=save_dir
        ), OpenAIWhisperParserLocal())
    else:
        loader = GenericLoader(YoutubeAudioLoader(
            urls=url,
            save_dir=save_dir, 
        ), OpenAIWhisperParser())
        
    docs = loader.load()
    
    combined_docs = [doc.page_content for doc in docs]
    text = " ".join(combined_docs)
    
    # splitter
    text_spitter = RecursiveCharacterTextSplitter(
        chunk_size = 1500,
        chunk_overlap=300
    )
    
    splits = text_spitter.split_text(text=text)
    
    # Build embedding and index
    embedding_function = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    
    vectordb = Chroma.from_texts(
        splits,
        embedding=embedding_function,
        persist_directory="vector_store_003",
        collection_name="google_cloud"
    )
    
except Exception as e:
    print(e)

