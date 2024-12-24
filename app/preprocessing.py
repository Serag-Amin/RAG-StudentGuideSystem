from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import Config

def load_pdf():
    loader = PyPDFLoader(Config.PDF_PATH)  # Ensure Config.PDF_PATH is correct
    return loader.load()

def split_documents(pages):
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )
    return splitter.split_documents(pages)
