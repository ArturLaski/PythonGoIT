import sys

def parse_args():
    # Join command-line arguments into a single string separated by spaces
    return ' '.join(sys.argv[1:])

# Example usage:
args_string = parse_args()
print("Command-line arguments:", args_string)