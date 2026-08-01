import numpy as np
from openai import OpenAI
from pypdf import PdfReader

client = OpenAI()

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts raw string text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text.strip()

def calculate_cosine_similarity(text1: str, text2: str) -> float:
    """Calculates semantic similarity score between two texts using vector embeddings."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[text1, text2]
    )
    vec1 = np.array(response.data[0].embedding)
    vec2 = np.array(response.data[1].embedding)
    
    similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    return float(similarity)
