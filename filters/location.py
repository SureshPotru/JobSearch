from config import LOCATION_KEYWORDS

def location_match(text: str) -> bool:
    t = text.lower()
    return any(loc in t for loc in LOCATION_KEYWORDS)
