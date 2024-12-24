import google.generativeai as genai
from prompts import Prompts

class SearchEngine:
    def __init__(self, db_manager):
        self.db = db_manager
        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")

    def process_query(self, user_query):
        # 1. Initial retrieval for question refinement
        initial_docs = self.search(user_query)
        
        # 2. Get refinement questions
        refinement_response = self.refine_search(user_query, initial_docs)
        questions = [user_query] + self._parse_questions(refinement_response)
        print(questions)
        # 3. Retrieve documents for all questions
        all_documents = set()
        for question in questions:
            docs = self.search(question)
            all_documents.update(docs)
        
        # 4. Generate final response
        final_response = self.generate_response(user_query, list(all_documents))
        return final_response

    def search(self, query):
        results = self.db.query(query, n_results=7)  
        documents = [doc["page_content"] for doc in results]  
        return documents

    def generate_response(self, query, documents):
        print(documents)
        prompt = Prompts.get_final_answer_prompt(query, documents)
        response = self.model.generate_content(prompt)
        return response.text

    def refine_search(self, query, documents):
        prompt = Prompts.get_search_refinement_prompt(query, documents)
        response = self.model.generate_content(prompt)
        return response.text

    def _parse_questions(self, refinement_text):
        # Split by newlines and filter empty lines
        return [line.strip() for line in refinement_text.split('\n') if line.strip()]
