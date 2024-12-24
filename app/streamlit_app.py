import streamlit as st
from main import initialize_system

st.title("Student Guide RAG System")

# # Debugging: Add a placeholder to verify progress
# debug_placeholder = st.empty()

def get_search_engine():
    # debug_placeholder.write("Initializing search engine...")
    return initialize_system()

# Initialize system
search_engine = get_search_engine()

# User input for query
query = st.text_input("Enter your question:", key="user_query")

if query:
    #debug_placeholder.write(f"Processing query: {query}")
    try:
        # Process the query and get a response
        response = search_engine.process_query(query)
        if response:
            st.write(response)
        else:
            st.write("No response received. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
