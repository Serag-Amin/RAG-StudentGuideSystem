import os
from dotenv import load_dotenv
import streamlit as st

# load_dotenv()

class Config:
    PDF_PATH = os.getenv('PDF_PATH', 'data/FCDS_guide.pdf')
    CHUNK_SIZE = 1500
    CHUNK_OVERLAP = 75
    DB_NAME = "vectdb"
    N_RESULTS = 7
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "No API key found")