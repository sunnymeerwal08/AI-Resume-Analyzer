import pandas as pd

def recommend_jobs(jobs, skills):
    if not skills:
        return []

    recommended = []
    for _, row in jobs.iterrows():
        job_skills = row["skills_required"].split(",") if "skills_required" in row else []
        job_skills = [s.strip().lower() for s in job_skills]

        matched = [skill for skill in skills if skill.lower() in job_skills]
        if matched:
            recommended.append({
                "title": row["job_title"],
                "company": row["company"],
                "location": row["location"],
                "skills_matched": matched
            })

    return recommended
