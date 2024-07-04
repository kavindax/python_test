# Problem 4: Dictionary Manipulation

def sort_dict_by_values(d : dict) -> dict:
    # Use sorted() function with a lambda function to sort the dictionary by values
    sorted_dict = dict(sorted(d.items(), key = lambda x: x[1]))
    return sorted_dict

d = {'a': 2, 'b': 1, 'c': 3}
print("Original Dictionary: ", d)
print("Sorted Dictionary by Values: ", sort_dict_by_values(d))
