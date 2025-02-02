#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()



#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

#Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

#Add the __init__() function to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.



#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)



class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)




class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019



class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)


#Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)