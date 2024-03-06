def split_list(grade):
    if not grade:  # Check if the list is empty
        return [], []
    
    average = sum(grade) / len(grade)
    lower_equal_avg = [score for score in grade if score <= average]
    greater_than_avg = [score for score in grade if score > average]
    
    return lower_equal_avg, greater_than_avg
    
    
        
            