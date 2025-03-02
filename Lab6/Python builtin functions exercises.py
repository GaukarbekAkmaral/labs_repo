import math
import time
import functools

def multiply_list(numbers):
    """Multiplies all numbers in a list using a built-in function."""
    return functools.reduce(lambda x, y: x * y, numbers)

def count_case_letters(text):
    """Counts uppercase and lowercase letters in a given string."""
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    return upper_count, lower_count

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    return s == s[::-1]

def delayed_square_root(number, delay):
    """Calculates square root of a number after a given delay in milliseconds."""
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")

def all_true(elements):
    """Returns True if all elements in the tuple are True."""
    return all(elements)

# Example usage:
# print(multiply_list([2, 3, 4]))
# print(count_case_letters("Hello World!"))
# print(is_palindrome("madam"))
# delayed_square_root(25100, 2123)
# print(all_true((True, True, False)))
