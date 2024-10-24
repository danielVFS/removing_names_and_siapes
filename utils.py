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
