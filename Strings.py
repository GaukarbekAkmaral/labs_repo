print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
#Get the characters from the start to position 5 (not included):
c = "Hello, World!"
print(c[:5])
#Get the characters from position 2, and all the way to the end:
d = "Hello, World!"
print(d[2:])
#From: "o" in "World!" (position -5). To, but not included: "d" in "World!" (position -2):
f = "Hello, World!"
print(f[-5:-2])
#The upper() method returns the string in upper case:
s = "Hello, World!"
print(s.upper())
#The lower() method returns the string in lower case:
k = "Hello, World!"
print(k.lower())
#The strip() method removes any whitespace from the beginning or the end:
g = " Hello, World! "
print(g.strip()) # returns "Hello, World!"
#The replace() method replaces a string with another string:
m = "Hello, World!"
print(m.replace("H", "J"))
#The split() method splits the string into substrings if it finds instances of the separator:
h = "Hello, World!"
print(h.split(",")) # returns ['Hello', ' World!']
#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt1 = f"The price is {20 * 59} dollars"
print(txt1)