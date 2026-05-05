#What is OOP?
#OOP stands for Object-Oriented Programming.

#Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

#Advantages of OOP
#Provides a clear structure to programs
#Makes code easier to maintain, reuse, and debug
#Helps keep your code DRY (Don't Repeat Yourself)
#Allows you to build reusable applications with less code
#Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

#What are Classes and Objects?
#Classes and objects are the two core concepts in object-oriented programming.

#A class defines what an object should look like, and an object is created based on that class. For example:

#Class	Objects
#Fruit	Apple, Banana, Mango
#Car	Volvo, Audi, Toyota

#Python Classes/Objects
#Python is an object oriented programming language.

#Almost everything in Python is an object, with its properties and methods.

#A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:
#class MyClass:
#  x = 5

#Create Object
#Now we can use the class named MyClass to create objects:

#Create an object named p1, and print the value of x:

#p1 = MyClass()
#print(p1.x)

#Delete Objects
#You can delete objects by using the del keyword:

#Example
#Delete the p1 object:

#del p1

#Python __init__() Method

#The __init__() Method
#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

#Create a class named Person, use the __init__() method to assign values for name and age:

#class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age

#p1 = Person("Emil", 36)

#print(p1.name)
#print(p1.age)

#Note: The __init__() method is called automatically every time the class is being used to create a new object.

#Default Values in __init__()
#You can also set default values for parameters in the __init__() method:

#class Person:
#  def __init__(self, name, age=18):
#    self.name = name
#    self.age = age

#p1 = Person("Emil", 36)

#print(p1.name)
#print(p1.age)

#The self Parameter
#The self parameter is a reference to the current instance of the class.

#It is used to access properties and methods that belong to the class.


# Use self to access class properties:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def greet(self):
#     print("Hello, my name is " + self.name)

# p1 = Person("Emil", 25)
# p1.greet()

# Note: The self parameter must be the first parameter of any method in the class.

# Why Use self?
# Without self, Python would not know which object's properties you want to access:

# Note: While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.

# Accessing Properties with self
# You can access any property of the class using self:

# class Car:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

#   def display_info(self):
#     print(f"{self.year} {self.brand} {self.model}")

# car1 = Car("Toyota", "Corolla", 2020)
# car1.display_info()

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     return "Hello, " + self.name

#   def welcome(self):
#     message = self.greet()
#     print(message + "! Welcome to our website.")

# p1 = Person("Tobias")
# p1.welcome()

# Class Propeties

# Properties are variables that belong to a class. They store data for each object created from the class.

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# Access Properties
# You can access object properties using dot notation:

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

# car1 = Car("Toyota", "Corolla")

# print(car1.brand)
# print(car1.model)

# Modify Properties
# You can modify the value of properties on objects:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Tobias", 25)
# print(p1.age)

# p1.age = 26
# print(p1.age)

# Delete Properties
# You can delete properties from objects using the del keyword:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Linus", 30)

# del p1.age

# print(p1.name) # This works
# # print(p1.age) # This would cause an error

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
  
#   class Person:
#   species = "Human" # Class property

#   def __init__(self, name):
#     self.name = name # Instance property

# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)

# class Person:
#   lastname = ""

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes"

# print(p1.lastname)
# print(p2.lastname)


# Add New Properties
# You can add new properties to existing objects:

# Example
# Add a new property to an object:

# class Person:
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")

# p1.age = 25
# p1.city = "Oslo"

# print(p1.name)
# print(p1.age)
# print(p1.city)

# Note: Adding properties this way only adds them to that specific object, not to all objects of the class.


# class Playlists:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)
#         print(f"{song} has been added")

#     def del_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"{song} has been removed")

#     def show_song(self):
#         print(f"{self.name}")
#         for s in self.songs:
#             print(f"songs - {s}")

# my_playlist = Playlists("favourites")            
# my_playlist.add_song("abc")
# my_playlist.add_song("xyz")
# my_playlist.show_song()


# class Personal():
#     def __init__(self):
#         self.info = {}

#     def add_info(self,id, name, age, work):
#         self.info[id] = {
#             "name" : name,
#             "age" : age,
#             "work" : work
#         }

#     def get_info(self, id):
#         return  self.info.get(id, "no records found")

#     def show_all(self):
#         for id, items in self.info.items():
#             print(f" Name : {(items['name'])}, Age : {(items['age'])}, Work : {(items['work'])}")


    
# p1 = Personal()
# p1.add_info(1,"tejas", 25, "developer")
# p1.add_info(2,"harsh", 25, "developer")
# p1.show_all()
# print(p1.get_info(5))

class dog:

    def __init__(self):
        self.info = {}

    def add_info(self, id, name, breed):
        self.info[id] = {
            "name" : name,
            "breed" : breed
        }

    def get_info(self, id):
        return self.info.get(id, "no records found")
    
    def show_all(self):
        for id, values in self.info.items():
            print(f" Name : {(values['name'])}, Breed : {(values['breed'])}")


dog = dog()

n = int(input("enter how many data you want to add: "))

for i in range(n):
    print(f"enter the details below {i+1}")
    
    id = int(input("Enter Id: "))
    name = input("Enter name: ")
    breed = input("Enter breed: ")
    
    dog.add_info(id, name, breed)    
         
    print("Below is the list of all the dogs")
    dog.show_all()
# print(dog.get_info(1))
