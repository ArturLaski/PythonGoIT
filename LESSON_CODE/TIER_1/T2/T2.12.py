message = "Hello my little friends!"
offset = 37
encoded_message = ""
for ch in message:
    if ch >= 'a' and ch <= 'z':
        pos = ord(ch) - ord('a')
        pos2 = (pos + offset) % 26
        new_char = chr(pos2 + ord("a"))
        encoded_message += new_char 
        print(f'char: {ch} {pos} {pos2} {new_char}')
    elif ch >= 'A' and ch <= 'Z':
        pos = ord(ch) - ord('A')
        pos2 = (pos + offset) % 26
        new_char = chr(pos2 + ord("A"))
        encoded_message += new_char 
        print(f'char: {ch} {pos} {pos2} {new_char}')
    else:
        encoded_message += ch
print(f"The original message: {message}")
print(f"The encoded message with offset {offset}: {encoded_message}")