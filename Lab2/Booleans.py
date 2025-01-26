print(10 > 9) #True
print(10 == 9)  #False
print(10 < 9)   #False

#Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Print the answer of a function:
def myFunction() :
  return True
print(myFunction())

#You can execute code based on the Boolean answer of a function:
#Print "YES!" if the function returns True, otherwise print "NO!"
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) #return True