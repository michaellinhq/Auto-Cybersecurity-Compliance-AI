import os
# from langchain.llms import OpenAI  # Uncomment when you have API Key
# from langchain.document_loaders import TextLoader
# from langchain.indexes import VectorstoreIndexCreator

"""
Compliance-Wächter MVP - Prototype v0.1
Author: [Your Name]
Description: A simple RAG (Retrieval-Augmented Generation) demo 
to query ISO 21434 clauses using natural language.
"""

def simple_compliance_query(user_question):
    """
    Mock function to demonstrate the logic of RAG for Compliance.
    In production, this will connect to a Vector Database (ChromaDB)
    containing the full text of UN R155 and ISO 21434.
    """
    
    # 1. Simulate retrieving relevant context from ISO 21434 (The "Retrieval" part)
    # In a real app, this comes from the Vector DB based on semantic similarity.
    retrieved_context = """
    [ISO/SAE 21434 Clause 15.4.1] 
    The organization shall evaluate the supplier's capability to develop 
    and produce the item in accordance with the cybersecurity requirements.
    """
    
    print(f"🔍 Analyzing Document Context: {retrieved_context.strip()}...\n")
    
    # 2. Simulate sending to LLM (The "Generation" part)
    print(f"🤖 AI Agent Thinking: How to answer '{user_question}' based on regulations...\n")
    
    # 3. Simulated Output
    answer = (
        f"Based on ISO 21434, regarding your question '{user_question}':\n"
        "You must perform a formal evaluation of your supplier's capability. "
        "Simply signing an NDA is not enough; you need evidence of their "
        "Cybersecurity capabilities (Clause 15.4.1)."
    )
    
    return answer

if __name__ == "__main__":
    # Test the logic
    question = "Do I need to audit my Tier-2 battery supplier?"
    response = simple_compliance_query(question)
    print("✅ Final Response:\n" + response)

    # TODO: 
    # 1. Connect to actual OpenAI/Gemini API key
    # 2. Load 'ISO21434_Summary.pdf' into ChromaDB
