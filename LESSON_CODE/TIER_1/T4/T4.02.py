def prepare_data(data):
    data_to_sort = data.copy()
    data_to_sort.remove(max(data_to_sort))
    data_to_sort.remove(min(data_to_sort))
    sorted_data = sorted(data_to_sort)
    return (sorted_data)
    
    
    
    
    