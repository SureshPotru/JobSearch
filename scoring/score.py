from config import PRIMARY_SKILLS, SECONDARY_SKILLS

def score_job(description: str) -> int:
    desc = description.lower()
    score = 0

    for skill, value in PRIMARY_SKILLS.items():
        if skill in desc:
            score += value

    for skill, value in SECONDARY_SKILLS.items():
        if skill in desc:
            score += value

    return min(score, 100)
