from config import MANDATORY_SKILLS

def has_mandatory_skills(description: str) -> bool:
    desc = description.lower()
    return all(skill in desc for skill in MANDATORY_SKILLS)
