# 1) String manipulation class
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

# 2) Shape and Square classes
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# 3) Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# 4) Point class
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# 5) Bank account class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

# 6) Filter prime numbers using filter and lambda
def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

# Example usage:
# 1)
string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()

# 2)
square = Square(5)
print(f"Square area: {square.area()}")

# 3)
rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")

# 4)
point1 = Point(1, 2)
point2 = Point(4, 6)
point1.show()
point1.move(3, 4)
point1.show()
print(f"Distance between points: {point1.dist(point2)}")

# 5)
account = Account("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)

# 6)
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = filter_primes(numbers)
print(f"Prime numbers: {prime_numbers}")