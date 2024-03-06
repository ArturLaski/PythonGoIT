def sanitize_file(source, output):
    try:
        # Open the source file for reading
        with open(source, "r") as source_file:
            # Read the contents of the source file
            source_content = source_file.read()

        # Remove digits from the content
        sanitized_content = ''.join(char for char in source_content if not char.isdigit())

        # Write the sanitized content to the output file
        with open(output, "w") as output_file:
            output_file.write(sanitized_content)

        print("File sanitized successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
source_file_path = "source.txt"
output_file_path = "output.txt"
sanitize_file(source_file_path, output_file_path)