from pydantic import BaseModel, Field
from typing import List

class SkillsAnalysis(BaseModel):
    matched_skills: List[str] = Field(description="Skills found in both resume and job description.")
    missing_skills: List[str] = Field(description="Crucial skills listed in JD but missing from resume.")

class BulletImprovement(BaseModel):
    original: str = Field(description="Weak bullet point from original resume.")
    improved: str = Field(description="Rewritten bullet point using strong action verbs and quantified metrics.")

class ResumeEvaluation(BaseModel):
    ats_score: int = Field(description="Estimated ATS compatibility score from 0 to 100.")
    candidate_summary: str = Field(description="2-3 sentence overview of candidate suitability.")
    skills: SkillsAnalysis
    bullet_improvements: List[BulletImprovement]
    actionable_recommendations: List[str] = Field(description="Specific steps to improve candidate match.")
