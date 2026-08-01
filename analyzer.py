from openai import OpenAI
from schema import ResumeEvaluation
from embeddings import calculate_cosine_similarity, extract_text_from_pdf

client = OpenAI()

def analyze_resume(pdf_path: str, job_description: str) -> ResumeEvaluation:
    # 1. Parse text from PDF
    resume_text = extract_text_from_pdf(pdf_path)
    
    # 2. Calculate baseline semantic similarity score
    semantic_match = calculate_cosine_similarity(resume_text, job_description)
    
    # 3. System Prompt specifying recruiter role and guidelines
    system_prompt = """
    You are an expert Technical Recruiter and ATS Optimization Assistant.
    Analyze the provided Resume against the target Job Description.
    Evaluate technical skills, experience alignment, and metric impact.
    Provide actionable feedback with concrete bullet point rewrites.
    """
    
    user_prompt = f"""
    [JOB DESCRIPTION]
    {job_description}

    [RESUME TEXT]
    {resume_text}

    Semantic Similarity Baseline: {round(semantic_match * 100, 2)}%
    
    Please evaluate the resume and output strict structured analysis matching the requested schema.
    """

    # 4. Enforce Pydantic schema using Structured Outputs
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format=ResumeEvaluation,
    )

    return completion.choices[0].message.parsed
