#Problem 3: File I/O
#Write a function that reads a text file, counts the number of words in it, and returns the count

def count_words_in_file(file_path : str) -> int:    
    with open(file_path, 'r') as file:
        words = file.read().split()
        return len(words)
    
file_path = "sample.txt"
print("Number of words in the file: ", count_words_in_file(file_path))

