def extract_skills(text):
   
    words = text.lower().replace(",", " ").split()
    keywords = {"python", "java", "c++", "sql", "excel", "communication", "teamwork"}
    found = {word.capitalize() for word in words if word in keywords}
    return found

def add_resume(applicant_id, resume_text, database):
    aid = (applicant_id,)  # Immutable tuple
    if aid in database:
        print(f"Applicant {applicant_id} already exists.")
        return

    skills = extract_skills(resume_text)
    database[aid] = {
        "resume": resume_text,
        "skills": skills
    }
    print(f"Resume for applicant {applicant_id} analyzed and stored.")

def view_resumes(database):
    if not database:
        print("No resumes stored.")
        return

    print("\n--- Resume Database ---")
    for aid, info in database.items():
        print(f"Applicant ID: {aid[0]}")
        print(f"Skills: {', '.join(info['skills'])}")
        print("-" * 30)
