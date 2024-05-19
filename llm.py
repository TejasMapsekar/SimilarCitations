"""
llm.py: Contains functions to find similar sources using a sentence transformer model
"""
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load pre-trained sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def find_similar_sources(data):
    """
    Find similar sources for each response in the data.

    Args:
        data (list): List of response and source data.

    Returns:
        list: List of responses with their similar citations.
    """
    results = []
    
    for item in data:
        response_text = item.get('response', '')
        response_embedding = model.encode(response_text, convert_to_tensor=True)
        
        citations = []
        for source in item.get('source', []):
            source_embedding = model.encode(source.get('context', ''), convert_to_tensor=True)
            similarity_score = util.pytorch_cos_sim(response_embedding, source_embedding).item()
            
            if similarity_score >= 0.5:  # Adjust threshold as needed
                citation = {'id': source['id'], 'similarity': similarity_score}
                if 'link' in source:
                    citation['link'] = source['link']
                citations.append(citation)
        
        results.append({'response': response_text, 'citations': citations})
    
    return results
