def capitalize_words(text):
    return " ".join([word.capitalize() for word in text.split()])
def reverse_string(text):
    return text[::-1]

def word_count(text):
    return len(text.split())