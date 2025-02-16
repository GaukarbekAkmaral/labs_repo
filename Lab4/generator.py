#1 Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2  # Yield the square of the number

# Example usage
N = 10
squares = square_generator(N)

# Print the generated squares
for square in squares:
    print(square)



#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(0, n + 1, 2):  # Generate even numbers from 0 to n
        yield str(i)  # Convert to string for easy joining

# Get user input
n = int(input("Enter a number: "))

# Generate and print even numbers in comma-separated form
print(", ".join(even_generator(n)))



#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i  # Yield numbers divisible by both 3 and 4

# Get user input
n = int(input("Enter a number: "))

# Iterate and print numbers from the generator
for num in divisible_by_3_and_4(n):
    print(num, end=" ")



#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2  # Yield the square of each number

# Get user input for range
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

# Test the generator with a for loop
print("Squares from", a, "to", b, ":")
for square in squares(a, b):
    print(square)



#5 Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    for i in range(n, -1, -1):  # Iterate from n down to 0
        yield i

# Get user input
n = int(input("Enter a number: "))

# Test the generator with a for loop
print("Countdown from", n, "to 0:")
for num in countdown(n):
    print(num)
