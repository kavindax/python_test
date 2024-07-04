#Problem 2: List Comprehensions


def square_of_even_numbers(numbers : list) -> list:
    # Use list comprehension to get the squares of even numbers
    squares =  [num**2 for num in numbers if num % 2 == 0]  # num**2 is the square of the number 
    return squares   

numbers = [1, 2, 3, 4, 5]

print("Original List: ", numbers)
print("Squares of Even Numbers: ", square_of_even_numbers(numbers))
# Output: [4, 16, 36, 64, 100]