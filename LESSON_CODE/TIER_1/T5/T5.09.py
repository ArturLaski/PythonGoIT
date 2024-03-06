import re

def find_all_words(text, word):
    # Compile a regex pattern to search for the word with any case variation
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    # Find all occurrences of the word in the text
    matches = pattern.findall(text)
    return matches

# Example usage:
text = "Python is a multi-paradigm programming language. python, PYTHON, PythOn, PyThOn, pyTHon, pYtHoN are all variations of the word Python."
word = "Python"
result = find_all_words(text, word)
print(result)