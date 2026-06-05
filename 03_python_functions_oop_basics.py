# Day 3: Python Functions and OOP Basics

# -------------------------------
# Python Functions
# -------------------------------

def greet():
    print("Hello, welcome to Python learning!")

greet()


# -------------------------------
# Function with Parameters
# -------------------------------

def greet_user(name):
    # Best Practice: f-string वापरल्याने कोड वाचायला सोपा होतो
    print(f"Hello, {name}")

greet_user("Shubham")


# -------------------------------
# Function with Multiple Arguments
# -------------------------------

def add_numbers(a, b):
    result = a + b
    print(f"Addition: {result}")

add_numbers(10, 20)


# -------------------------------
# Function with Return Value
# -------------------------------

def multiply_numbers(a, b):
    return a * b

answer = multiply_numbers(5, 4)
print(f"Multiplication: {answer}")


# -------------------------------
# *args in Python
# -------------------------------

def total_marks(*marks):
    # Best Practice: loop ऐवजी डायरेक्ट sum() फंक्शन वापरून कोड छोटा केला
    total = sum(marks)
    print(f"Total Marks: {total}")

total_marks(80, 75, 90, 85)


# -------------------------------
# Python Class and Object
# -------------------------------

class Student:
    # Best Practice: प्रत्येक ऑब्जेक्टसाठी डेटा वेगळा ठेवण्यासाठी __init__ वापरणे योग्य असते
    def __init__(self, name="Shubham", course="Python"):
        self.name = name
        self.course = course

# Creating object
student1 = Student()

print(f"Student Name: {student1.name}")
print(f"Course: {student1.course}")


# -------------------------------
# __init__ Constructor and self
# -------------------------------

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Role: {self.role}")

employee1 = Employee("Shubham", "Software Engineer")
employee1.display_details()


# -------------------------------
# Class with Methods
# -------------------------------

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()

print(f"Addition Result: {calc.add(15, 5)}")
print(f"Subtraction Result: {calc.subtract(15, 5)}")


# -------------------------------
# Multiple Constructor-like Behavior
# Using Default Arguments
# -------------------------------

class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

person1 = Person()
person2 = Person("Shubham")
person3 = Person("Shubham", 25)

person1.show_info()
person2.show_info()
person3.show_info()


# -------------------------------
# Multiple Constructor-like Behavior
# Using Class Method
# -------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, product_string):
        name, price = product_string.split("-")
        return cls(name, int(price))

    def show_product(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")

product1 = Product("Laptop", 50000)
product2 = Product.from_string("Mobile-20000")

product1.show_product()
product2.show_product()
