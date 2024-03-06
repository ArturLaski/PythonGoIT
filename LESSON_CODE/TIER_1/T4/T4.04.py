def lookup_key(data, value):
  key_list = []
  for lab, val in data.items():
    if val == value:
      key_list.append(lab)
  return key_list

data = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
search_key = 2
result = lookup_key(data, search_key)
print(f"Keys with value {search_key}: {result}")
            
    