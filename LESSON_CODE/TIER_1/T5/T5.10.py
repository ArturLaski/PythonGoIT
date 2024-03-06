import re

def replace_spam_words(text, spam_words):
    # Compile a regex pattern to search for all stop words with any case variation
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, spam_words)) + r')\b', re.IGNORECASE)
    # Replace all occurrences of stop words with asterisks of the same length
    replaced_text = pattern.sub(lambda x: '*' * len(x.group()), text)
    return replaced_text

# Example usage:
text = "This message contains some bad words like bad, Bad, BaD, and BAD."
spam_words = ["bad", "rude", "offensive"]
result = replace_spam_words(text, spam_words)
print(result)