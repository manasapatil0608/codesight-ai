def score_file(keywords, filename):
    filename = filename.lower()
    score = 0.0

    # Keyword match weight
    for kw in keywords:
        if kw in filename:
            score += 0.5

    # Folder hints
    if "auth" in filename and any(kw in ["login", "otp", "auth"] for kw in keywords):
        score += 0.2

    if "payment" in filename and any(kw in ["payment", "checkout", "refund"] for kw in keywords):
        score += 0.2

    if "notification" in filename and any(kw in ["email", "sms", "push"] for kw in keywords):
        score += 0.2

    # File type weighting
    if filename.endswith(".js"):
        score += 0.1

    if ".test" in filename:
        score -= 0.1

    if filename.endswith(".md"):
        score -= 0.15

    # Clamp score
    return round(max(0.0, min(score, 1.0)), 2)
