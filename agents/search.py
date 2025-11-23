def search_files(keywords, file_list):
    """
    Finds files that contain any of the keywords in their path.
    """
    candidates = []

    for file_path in file_list:
        lower_path = file_path.lower()
        for kw in keywords:
            if kw in lower_path:
                candidates.append(file_path)

    return list(set(candidates))
