def real_len(text):
    bad_chars = {'\n', '\f', '\r', '\t', '\v'}
    return len(''.join(i for i in text if not i in bad_chars))