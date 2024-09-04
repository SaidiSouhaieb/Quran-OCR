import re


def filter_text(text):
    filtered_text = re.sub(r"[0-9|]", "", text)
    filtered_text = filtered_text.strip()
    return filtered_text.replace("\n", "")
