# 13. Resume Skill Matcher

# Description: Match job profiles with resumes.
# Requirements:
# - {resume_id: {"skills": [...], "experience": ...}}
# - Search resumes with required skills
# - Filter by experience range
# - Use .values() and in for filtering

resumes = {
    101: {"skills": ["Python", "Django", "SQL"], "experience": 3},
    102: {"skills": ["Java", "Spring", "SQL"], "experience": 5},
    103: {"skills": ["Python", "Flask", "JavaScript"], "experience": 2},
    104: {"skills": ["JavaScript", "React", "Node.js"], "experience": 4},
}

def match_resumes(required_skills, min_experience):
    """Match resumes based on required skills and minimum experience."""
    return {
        resume_id: details
        for resume_id, details in resumes.items()
        if all(skill in details["skills"] for skill in required_skills)
        and details["experience"] >= min_experience
    }

def count_matching_resumes(required_skills, min_experience):
    """Count resumes matching required skills and minimum experience."""
    return sum(
        all(skill in details["skills"] for skill in required_skills)
        and details["experience"] >= min_experience
        for details in resumes.values()
    )

required_skills = ["Python", "SQL"]
min_experience = 3
matching_resumes = match_resumes(required_skills, min_experience)
matching_count = count_matching_resumes(required_skills, min_experience)

print(f"Matching Resumes: {matching_resumes}")
print(f"Number of Matching Resumes: {matching_count}")
