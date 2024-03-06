def file_operations (path, additional_info,  start_pos, count_chars) :
    with open (path, 'a') as f: 
        f.write(additional_info)
    with open (path, 'r') as f: 
        f. seek(start_pos) 
        result_string  = f.read(count_chars)
    return result_string