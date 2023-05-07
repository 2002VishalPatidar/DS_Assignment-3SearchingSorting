def sort_list_of_strings(lst):
    return sorted(lst, key=lambda s: s.lower())
lst = ['Govind', 'Vishal', 'Ankit']
print(sort_list_of_strings(lst))
