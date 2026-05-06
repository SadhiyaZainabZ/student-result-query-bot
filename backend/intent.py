def detect_intent(query: str):
    q = query.lower()

    if "marks" in q:
        return "marks"

    if "attendance" in q:
        return "attendance"

    if "topper" in q or "highest" in q:
        return "topper"

    return "general"