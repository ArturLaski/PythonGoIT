def all_sub_lists(data):
    sub_lists = [[]]  # Initialize with an empty sublist
    
    for i in range(1, len(data)+1):
        for j in range(0 , len(data) - i + 1):
            sublists = data[j : j+i]
            sub_lists.append(sublists)  # Append sublists to the result list
    return sub_lists