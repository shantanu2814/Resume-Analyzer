import json
from analyzer import analyze_resume

if __name__ == "__main__":
    job_desc = """
    We are looking for a Senior Python AI Engineer with experience in building LLM applications,
    FastAPI microservices, vector databases, and PyTorch. Candidate must have strong knowledge 
    of system design, structured outputs, and CI/CD pipelines.
    """
    
    # Run analysis on candidate resume
    results = analyze_resume("sample_resume.pdf", job_desc)
    
    print("\n--- 📊 RESUME ANALYSIS RESULTS ---")
    print(f"ATS Score: {results.ats_score}/100")
    print(f"\nSummary:\n{results.candidate_summary}")
    
    print("\n✅ Matched Skills:", ", ".join(results.skills.matched_skills))
    print("❌ Missing Skills:", ", ".join(results.skills.missing_skills))
    
    print("\n✍️ Suggested Bullet Improvements:")
    for item in results.bullet_improvements:
        print(f"  • Before: {item.original}")
        print(f"    After:  {item.improved}\n")
