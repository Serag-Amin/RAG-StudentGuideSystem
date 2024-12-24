import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class Config:
    PDF_PATH = os.getenv('PDF_PATH', 'data/FCDS_guide.pdf')
    CHUNK_SIZE = 1500
    CHUNK_OVERLAP = 75
    DB_NAME = "vectdb"
    N_RESULTS = 5

    # Get API key from environment variables or Streamlit secrets
    def get_google_api_key():
        if "GOOGLE_API_KEY" in os.environ:  # locally
            return os.getenv("GOOGLE_API_KEY")
        elif "GOOGLE_API_KEY" in st.secrets:  # Streamlit's secrets manager
            return st.secrets["GOOGLE_API_KEY"]
        else:
            raise ValueError("Google API key not found. Please set it in your environment or Streamlit secrets.")

google_api_key = get_google_api_key()