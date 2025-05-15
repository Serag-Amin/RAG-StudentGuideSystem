# RAG-StudentGuideSystem

A Retrieval-Augmented Generation (RAG) system that provides students and faculty with quick access to information on college rules, courses, and policies by searching the official student guide. The system supports both Arabic and English queries, ensuring accurate answers to save time and reduce confusion when seeking details like course information, evaluation systems, or academic procedures.

## Features

- Bilingual support (Arabic and English)
- Semantic search capabilities
- PDF document processing
- Interactive web interface
- Real-time question answering
- Context-aware responses

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google API key for Gemini AI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RAG-StudentGuideSystem.git
cd RAG-StudentGuideSystem
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Project Structure

```
RAG-StudentGuideSystem/
├── app/                    # Application code
├── data/                   # PDF documents and processed data
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
└── README.md              # Project documentation
```

## Usage

1. Place your PDF documents in the `data/` directory
2. Run the Streamlit application:
```bash
streamlit run app/app.py
```
3. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
4. Enter your questions in either Arabic or English
5. View the generated responses with relevant context

## Customizing the Data

To use your own documents:

1. Place your PDF files in the `data/` directory
2. The system will automatically process new documents on startup
3. Supported formats: PDF
4. For best results, ensure documents are properly formatted and text is extractable

## Dependencies

- google-generativeai: For AI-powered text generation
- sentence-transformers: For semantic text embeddings
- streamlit: For the web interface
- python-dotenv: For environment variable management
- PyPDF: For PDF processing
- langchain: For RAG implementation
- langchain-community: For additional LangChain components
- faiss-cpu: For vector similarity search
- numpy: For numerical operations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
