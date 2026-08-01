import os
from openai import OpenAI
from schema import ResumeEvaluation
from embeddings import calculate_cosine_similarity, extract_text_from_pdf

# Initialize client pointing to xAI's endpoint
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def analyze_resume(pdf_path: str, job_description: str) -> ResumeEvaluation:
    resume_text = extract_text_from_pdf(pdf_path)
    semantic_match = calculate_cosine_similarity(resume_text, job_description)

    completion = client.beta.chat.completions.parse(
        model=os.getenv("LLM_MODEL", "grok-2"),
        messages=[
            {
                "role": "system", 
                "content": "You are a Senior Recruiter. Analyze resumes strictly and give structured feedback."
            },
            {
                "role": "user", 
                "content": f"Job Description:\n{job_description}\n\nResume:\n{resume_text}"
            }
        ],
        response_format=ResumeEvaluation,
    )

    return completion.choices[0].message.parsed
