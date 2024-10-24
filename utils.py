import re
from itertools import combinations


def normalize_spaces(text):
    return re.sub(r'\s+', ' ', text)


def generate_combinations_of_name(parts):
    partial_names = set()
    for r in range(1, len(parts) + 1):
        for combo in combinations(parts, r):
            partial_name = ' '.join(combo)
            partial_names.add(partial_name)
    return partial_names


def replace_full_word_ignore_case(text, sub, replacement):
    pattern = r'\b' + re.escape(sub) + r'\b'
    return re.sub(pattern, replacement, text, flags=re.IGNORECASE)


def replace_ignore_case(text, sub, replacement):
    start = 0
    while True:
        start = text.lower().find(sub, start)
        if start == -1:
            return text
        text = text[:start] + replacement + text[start + len(sub):]
        start += len(replacement)
