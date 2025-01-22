x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Python allows you to assign values to multiple variables in one line:
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
q, y, u = fruits
print(q)
print(y)
print(u)
#And you can assign the same value to multiple variables in one line:
d = f = g = "Orange"
print(d)
print(f)
print(g)
