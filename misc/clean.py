def removeTags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def cutLength(text):
    if len(text) > 900:
        return text[:900] + "..."
    return text