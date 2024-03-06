def get_credentials_users(path):
    credentials_list = []
    with open(path, 'rb') as file:
        for line in file:
            credentials_list.append(line.strip().decode())
    return credentials_list

# Example usage:
credentials = get_credentials_users("user_credentials.bin")
print(credentials)