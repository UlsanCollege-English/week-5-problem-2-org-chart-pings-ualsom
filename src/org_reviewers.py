def count_senior(root, min_level):
    if root is None:
        return 0
    count = 1 if root.get("level", 0) >= min_level else 0
    for report in root.get("reports", []):
        count += count_senior(report, min_level)
    return count
