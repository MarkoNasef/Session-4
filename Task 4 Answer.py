# Task 1: Print each element of the list on its own line
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
    print(word)

# Task 2: Print multiples of 5 less than or equal to 30
for num in range(5, 31, 5):
    print(num)

# Task 3: Password Generator
import random

def generate_password_easy(letters_count, symbols_count, numbers_count):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password = (
        random.choices(letters, k=letters_count) +
        random.choices(symbols, k=symbols_count) +
        random.choices(numbers, k=numbers_count)
    )
    return "".join(password)

print(generate_password_easy(4, 2, 3))

def generate_password_hard(letters_count, symbols_count, numbers_count):
    password = generate_password_easy(letters_count, symbols_count, numbers_count)
    password = list(password)
    random.shuffle(password)
    return "".join(password)

print(generate_password_hard(4, 2, 3))

# Task 4: Factorial using While Loop
def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial_while(6))  # Output: 720

# Task 4: Factorial using For Loop
def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_for(6))  # Output: 720
