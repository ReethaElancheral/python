import json
import os

JSON_FILE = "resumes.json"

def load_resumes():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_resumes(resumes):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(resumes, f, indent=4)

def add_resume():
    name = input("Name: ").strip()
    skills = input("Skills (comma separated): ").strip().split(",")
    experience = input("Experience (years): ").strip()
    try:
        experience = float(experience)
    except ValueError:
        print("Invalid experience value.")
        return

    resumes = load_resumes()
    # Check if already exists
    for r in resumes:
        if r["name"].lower() == name.lower():
            print("Resume with this name already exists.")
            return

    new_resume = {
        "name": name,
        "skills": [s.strip() for s in skills if s.strip()],
        "experience": experience
    }
    resumes.append(new_resume)
    save_resumes(resumes)
    print("✅ Resume added.")

def search_resume():
    name = input("Enter name to search: ").strip()
    resumes = load_resumes()
    found = False
    for r in resumes:
        if r["name"].lower() == name.lower():
            print(f"\nName: {r['name']}")
            print(f"Skills: {', '.join(r['skills'])}")
            print(f"Experience: {r['experience']} years")
            found = True
            break
    if not found:
        print("Resume not found.")

def update_resume():
    name = input("Enter name to update: ").strip()
    resumes = load_resumes()
    for i, r in enumerate(resumes):
        if r["name"].lower() == name.lower():
            print(f"Current skills: {', '.join(r['skills'])}")
            new_skills = input("New skills (comma separated): ").strip().split(",")
            print(f"Current experience: {r['experience']} years")
            new_exp = input("New experience (years): ").strip()
            try:
                new_exp = float(new_exp)
            except ValueError:
                print("Invalid experience value.")
                return
            resumes[i]["skills"] = [s.strip() for s in new_skills if s.strip()]
            resumes[i]["experience"] = new_exp
            save_resumes(resumes)
            print("✅ Resume updated.")
            return
    print("Resume not found.")
