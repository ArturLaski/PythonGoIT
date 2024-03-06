import re

def find_word(text, word):
    result = {}
    
    match = re.search(re.escape(word), text)
    if match:
        result['result'] = True
        result['first_index'] = match.start()
        result['last_index'] = match.end()
    else:
        result['result'] = False
        result['first_index'] = None
        result['last_index'] = None
        
    result['search_string'] = word
    result['string'] = text    
    return result

# Example usage:
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))