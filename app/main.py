from preprocessing import load_pdf, split_documents
from database import FAISSManager  # Updated to FaissDBManager
from search import SearchEngine

def initialize_system():
    # Load and split PDF
    pages = load_pdf()
    chunks = split_documents(pages)
    
    # Initialize database manager and add documents
    db_manager = FAISSManager()  
    db_manager.add_documents(chunks)  # Ensure this adds documents to FAISS
    
    # Initialize the search engine
    search_engine = SearchEngine(db_manager)  # Pass FaissDBManager instance
    print("System initialized.")

    return search_engine

# Main Execution
if __name__ == "__main__":
    # Initialize system
    search_engine = initialize_system()
    
    # Get query from user input in terminal
    query = input("Enter your question: ")

    if query:
        # Process the query
        response = search_engine.process_query(query)  # Removed redundant argument
        # Print the response to the terminal
        print(f"Response: {response}")
