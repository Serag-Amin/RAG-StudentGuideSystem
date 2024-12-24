from preprocessing import load_pdf, split_documents
from database import FAISSManager  # Updated to FaissDBManager
from search import SearchEngine

def initialize_system():

    pages = load_pdf()
    chunks = split_documents(pages)
    
    # Initialize the database manager
    db_manager = FAISSManager()  
    db_manager.add_documents(chunks)  
    
    # Initialize the search engine
    search_engine = SearchEngine(db_manager)  
    print("System initialized.")

    return search_engine


if __name__ == "__main__":
    # Initialize the system
    search_engine = initialize_system()
    
    # User input for query
    query = input("Enter your question: ")

    if query:
        # Process the query
        response = search_engine.process_query(query)  # Removed redundant argument
        print(f"Response: {response}")
