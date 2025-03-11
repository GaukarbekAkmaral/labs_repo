# 1) Grams to ounces conversion
def grams_to_ounces(grams):
    """Converts grams to ounces.

    Args:
        grams: The weight in grams.

    Returns:
        The weight in ounces.
    """
    ounces = 28.3495231 * grams
    return ounces

# 2) Fahrenheit to Celsius conversion
def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature in Celsius.
    """
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# 3) Chickens and rabbits puzzle
def solve(numheads, numlegs):
    """Solves the chickens and rabbits puzzle.

    Args:
        numheads: The number of heads.
        numlegs: The number of legs.

    Returns:
        A tuple containing the number of chickens and rabbits.
    """
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None  # No solution

# 4) Prime number filter
def filter_prime(numbers):
    """Filters prime numbers from a list.

    Args:
        numbers: A list of numbers.

    Returns:
        A list containing only the prime numbers.
    """
    primes =
    for num in numbers:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

# 5) String permutations
def print_permutations(string):
    """Prints all permutations of a string.

    Args:
        string: The string to permute.
    """
    if len(string) == 1:
        print(string)
    else:
        for i in range(len(string)):
            char = string[i]
            remaining_chars = string[:i] + string[i+1:]
            for permutation in print_permutations(remaining_chars):
                print(char + permutation)

# 6) Reverse words in a sentence
def reverse_words(sentence):
    """Reverses the words in a sentence.

    Args:
        sentence: The sentence to reverse.

    Returns:
        The sentence with words reversed.
    """
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

# 7) Check for 3 next to 3
def has_33(nums):
    """Checks if a list contains a 3 next to a 3.

    Args:
        nums: The list of numbers.

    Returns:
        True if the list contains a 3 next to a 3, False otherwise.
    """
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 8) Check for 007 in order
def spy_game(nums):
    """Checks if a list contains 007 in order.

    Args:
        nums: The list of numbers.

    Returns:
        True if the list contains 007 in order, False otherwise.
    """
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

# 9) Volume of a sphere
def sphere_volume(radius):
    """Calculates the volume of a sphere.

    Args:
        radius: The radius of the sphere.

    Returns:
        The volume of the sphere.
    """
    from math import pi
    return (4/3) * pi * radius**3

# 10) Unique elements in a list
def unique_elements(lst):
    """Returns a new list with unique elements of the first list.

    Args:
        lst: The input list.

    Returns:
        A new list with unique elements.
    """
    unique_list =
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# 11) Palindrome check
def is_palindrome(text):
    """Checks whether a word or phrase is palindrome or not.

    Args:
        text: The word or phrase to check.

    Returns:
        True if the input is a palindrome, False otherwise.
    """
    processed_text = ''.join(c for c in text.lower() if c.isalnum())
    return processed_text == processed_text[::-1]

# 12) Histogram
def histogram(data):
    """Prints a histogram to the screen.

    Args:
        data: A list of integers.
    """
    for num in data:
        print("*" * num)

# 13) Guess the number game
def guess_the_number():
    """Plays the "Guess the number" game."""
    import random

    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
