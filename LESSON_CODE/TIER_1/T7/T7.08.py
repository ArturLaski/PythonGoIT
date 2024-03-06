def get_employees_by_profession(path, profession) : 
    with open (path,  'r' ) as file: 
        lines = file.readlines() 

    filtered = []
    for line in lines:
        if line.find(profession) >= 0:
            filtered.append(line.strip())
    
    oneline = ''.join(filtered)
    clear_result = oneline.replace(profession, "")
    return clear_result.strip()