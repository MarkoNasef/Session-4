# Task 1: Print each element of the list on its own line
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
    print(word)

# Task 2: Print multiples of 5 less than or equal to 30
for num in range(5, 31, 5):
    print(num)

# Task 3: Password Generator
import random

def generate_password_easy(letters, symbols, numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password = (
        random.choices(letters) +
        random.choices(symbols) +
        random.choices(numbers)
    )
    

# Task 4: Factorial using While Loop
def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial_while(6))  # Output: 720


