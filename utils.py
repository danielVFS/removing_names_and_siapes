import re


def normalize_spaces(text):
    return re.sub(r'\s+', ' ', text)
