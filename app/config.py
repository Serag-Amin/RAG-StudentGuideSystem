import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PDF_PATH = os.getenv('PDF_PATH', 'data/FCDS_guide.pdf')
    CHUNK_SIZE = 1500
    CHUNK_OVERLAP = 75
    DB_NAME = "vectdb"
    N_RESULTS = 5
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "default-api-key")  
