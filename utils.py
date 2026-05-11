def is_vague_query(text):

    vague_words = [
        "assessment",
        "test",
        "hire",
        "job"
    ]

    text = text.lower()

    if len(text.split()) <= 3:
        return True

    for word in vague_words:
        if text.strip() == word:
            return True

    return False


def is_comparison_query(text):

    text = text.lower()

    comparison_words = [
        "difference",
        "compare",
        "vs",
        "versus"
    ]

    return any(word in text for word in comparison_words)