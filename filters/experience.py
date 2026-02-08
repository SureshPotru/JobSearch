import re

def senior_role(description: str) -> bool:
    patterns = [
        r"8\+?\s*years",
        r"senior",
        r"lead",
        r"principal"
    ]
    desc = description.lower()
    return any(re.search(p, desc) for p in patterns)
