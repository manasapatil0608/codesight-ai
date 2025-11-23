from agents.impact import categorize_impact

def generate_report(scored_files):
    impact_map = {"High": [], "Medium": [], "Low": []}

    for file_path, score in scored_files.items():
        level = categorize_impact(score)
        impact_map[level].append((file_path, score))

    # Sort inside each category
    for level in impact_map:
        impact_map[level].sort(key=lambda x: x[1], reverse=True)

    return impact_map
