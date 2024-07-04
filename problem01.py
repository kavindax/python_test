# Problem 01 : Reverse a String

def reverse_string(s : str) -> str:
    # Use slicing to reverse the string. -  s[start:stop:step] 

    reversed_string = s[::-1]
    return reversed_string


string = "Hello World"
print("Original String: ", string)
print("Reversed String: ", reverse_string(string))

string = "Python"
print("Original String: ", string)
print("Reversed String: ", reverse_string(string))
