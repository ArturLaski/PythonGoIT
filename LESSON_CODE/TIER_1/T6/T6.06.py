def save_applicant_data(source, output):
    try:
        # Open the output file for writing
        with open(output, "w") as output_file:
            # Iterate over each applicant in the source list
            for applicant in source:
                # Extract applicant's information
                name = applicant["name"]
                specialty = str(applicant["specialty"])
                math_score = str(applicant["math"])
                lang_score = str(applicant["lang"])
                eng_score = str(applicant["eng"])
                
                # Construct the line to write to the file
                line = f"{name},{specialty},{math_score},{lang_score},{eng_score}\n"
                
                # Write the line to the output file
                output_file.write(line)
        
        print("Applicant data saved successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
applicants_list = [
    {"name": "Kovalchuk Oleksiy", "specialty": 301, "math": 175, "lang": 180, "eng": 155},
    {"name": "Ivanchuk Boryslav", "specialty": 101, "math": 135, "lang": 150, "eng": 165},
    {"name": "Karpenko Dmitro", "specialty": 201, "math": 155, "lang": 175, "eng": 185}
]

output_file_path = "applicant_data.txt"
save_applicant_data(applicants_list, output_file_path)