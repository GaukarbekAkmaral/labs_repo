#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

pattern = r'ab*'
test_strings = ["a", "ab", "abb", "ac", "b", "aabb"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#2. Match a string with 'a' followed by two to three 'b's
pattern = r'abb{2,3}'

test_strings = ["abb", "abbb", "abbbb", "a", "ab", "abbbbb"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#3. Find sequences of lowercase letters joined with an underscore
pattern = r'\b[a-z]+_[a-z]+\b'

test_strings = ["hello_world", "snake_case", "Hello_World", "lowercase_", "_underscore", "abc_def_ghi"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#4. Find a sequence of one uppercase letter followed by lowercase letters
pattern = r'[A-Z][a-z]+'

test_strings = ["Hello", "CamelCase", "UPPER", "lower", "Python", "A"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#5. Match a string with 'a' followed by anything, ending in 'b'
pattern = r'a.*b$'

test_strings = ["ab", "acb", "a123b", "abb", "b", "abc", "xyz"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#6. Replace all occurrences of space, comma, or dot with a colon
import re

text = "Hello, world. This is a test, string."
new_text = re.sub(r'[ ,.]', ":", text)

print(new_text)  # Output: Hello::world::This:is:a:test::string:

#7. Convert a snake_case string to camelCase
import re

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(snake_to_camel("hello_world"))  # Output: helloWorld
print(snake_to_camel("convert_snake_case"))  # Output: convertSnakeCase

#8. Split a string at uppercase letters
import re

def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)

print(split_at_uppercase("HelloWorldExample"))  # Output: ['Hello', 'World', 'Example']
print(split_at_uppercase("SplitAtUppercase"))  # Output: ['Split', 'At', 'Uppercase']

#9. Insert spaces between words starting with capital letters
import re

def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

print(insert_spaces("HelloWorldExample"))  # Output: "Hello World Example"
print(insert_spaces("SplitAtUppercase"))  # Output: "Split At Uppercase"

#10 Convert a given camelCase string to snake_case
import re

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

print(camel_to_snake("helloWorld"))  # Output: hello_world
print(camel_to_snake("convertCamelCase"))  # Output: convert_camel_case
