def parse_requirement(requirement: str):
    """
    Extracts meaningful keywords from the requirement text.
    """
    requirement = requirement.lower()
    keywords = []

    possible_keywords = [
        "login", "logout", "register", "auth", "authentication",
        "otp", "two-factor", "user", "profile",
        "payment", "checkout", "invoice", "refund",
        "notification", "email", "sms", "push"
    ]

    for word in possible_keywords:
        if word in requirement:
            keywords.append(word)

    return list(set(keywords))
