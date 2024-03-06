def is_equal_string(utf8_string, utf16_string):
    try:
        # Decode both strings into Unicode strings
        utf8_decoded = utf8_string.decode('utf-8')
        utf16_decoded = utf16_string.decode('utf-16')

        # Compare the decoded strings
        return utf8_decoded == utf16_decoded
    except Exception as e:
        print("An error occurred:", e)
        return False

# Example usage:
utf8_string = b'\xe2\x82\xac'  # Euro symbol encoded in UTF-8
utf16_string = b'\xff\xfe\xa2\x20'  # Euro symbol encoded in UTF-16

result = is_equal_string(utf8_string, utf16_string)
print("Strings are equal:", result)