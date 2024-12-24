import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PDF_PATH = os.getenv('PDF_PATH', 'data/FCDS_guide.pdf')
    CHUNK_SIZE = 1500
    CHUNK_OVERLAP = 75
    DB_NAME = "vectdb"
    N_RESULTS = 5

    # Get API key from environment variables or Streamlit secrets
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  
    if GOOGLE_API_KEY is None:
        raise ValueError("GOOGLE_API_KEY is not set. Please set it in the environment variables.")