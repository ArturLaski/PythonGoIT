def data_preparation(list_data):
    cleaned_data = []
    
    # Iterating over each list in the list_data
    for sublist in list_data:
        if len(sublist) > 2:  # Check if sublist has more than 2 elements
            # Remove minimum and maximum values
            sublist.remove(min(sublist))
            sublist.remove(max(sublist))
        cleaned_data.extend(sublist)  # Extend cleaned_data with the remaining elements
    
    # Sort the combined list in descending order
    result = sorted(cleaned_data, reverse=True)
    
    return result   