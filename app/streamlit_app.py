import streamlit as st
from main import initialize_system

st.title("Student Guide RAG System")

# Sidebar message to inform users about asking clear questions
st.sidebar.info(
    "🔍 **Tips for best results:**\n\n"
    "- Please be clear and concise when asking your question.\n"
    "- Avoid vague or too general questions.\n"
    "- For example, ask 'How do I apply for scholarships?' instead of just 'Tell me about scholarships.'"
)

# Sidebar message about the app being under development
st.sidebar.warning("⚠️ This app is still under development. Expect updates and improvements!")

def get_search_engine():
    return initialize_system()

# Initialize system
search_engine = get_search_engine()

# User input for query
query = st.text_input("Enter your question:", key="user_query")

if query:
    try:
        # Process the query and get a response
        response = search_engine.process_query(query)
        if response:
            st.write(response)
        else:
            st.write("No response received. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
