# Day 4: Advanced Python Concepts

from abc import ABC, abstractmethod
from functools import reduce


# -------------------------------
# Encapsulation
# -------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)

    def get_balance(self):
        return self.__balance


account = BankAccount("Shubham", 5000)
account.deposit(2000)
print("Account Holder:", account.account_holder)
print("Current Balance:", account.get_balance())


# -------------------------------
# Private Method
# -------------------------------

class LoginSystem:
    def __validate_password(self, password):
        return password == "admin123"

    def login(self, password):
        if self.__validate_password(password):
            print("Login Successful")
        else:
            print("Invalid Password")


login_user = LoginSystem()
login_user.login("admin123")


# -------------------------------
# Inheritance
# -------------------------------

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()
dog.bark()


# -------------------------------
# Multiple Inheritance
# -------------------------------

class Father:
    def father_quality(self):
        print("Father quality: Hardworking")


class Mother:
    def mother_quality(self):
        print("Mother quality: Caring")


class Child(Father, Mother):
    def child_quality(self):
        print("Child quality: Learning")


child = Child()
child.father_quality()
child.mother_quality()
child.child_quality()


# -------------------------------
# super() Method
# -------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def show_details(self):
        super().show_name()
        print("Role:", self.role)


employee = Employee("Shubham", "Software Engineer")
employee.show_details()


# -------------------------------
# Composition
# -------------------------------

class Engine:
    def start_engine(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start_engine()
        print("Car started")


car = Car()
car.start_car()


# -------------------------------
# Aggregation
# -------------------------------

class Department:
    def __init__(self, department_name):
        self.department_name = department_name


class Student:
    def __init__(self, student_name, department):
        self.student_name = student_name
        self.department = department

    def show_student_details(self):
        print("Student Name:", self.student_name)
        print("Department:", self.department.department_name)


department = Department("Computer Science")
student = Student("Shubham", department)
student.show_student_details()


# -------------------------------
# Abstract Class
# -------------------------------

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)
print("Rectangle Area:", rectangle.area())


# -------------------------------
# Exception Handling
# -------------------------------

try:
    number1 = 10
    number2 = 0
    result = number1 / number2

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

else:
    print("Division Result:", result)

finally:
    print("Exception handling completed")


# -------------------------------
# Python Iterator
# -------------------------------

numbers = [10, 20, 30]

number_iterator = iter(numbers)

print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))


# -------------------------------
# Python Generator
# -------------------------------

def generate_numbers():
    for number in range(1, 4):
        yield number


for value in generate_numbers():
    print("Generated Value:", value)


# -------------------------------
# Lambda Function
# -------------------------------

square = lambda number: number * number

print("Square:", square(5))


# -------------------------------
# map() Function
# -------------------------------

numbers_list = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number * number, numbers_list))

print("Squares using map:", squares)


# -------------------------------
# filter() Function
# -------------------------------

even_numbers = list(filter(lambda number: number % 2 == 0, numbers_list))

print("Even numbers using filter:", even_numbers)


# -------------------------------
# reduce() Function
# -------------------------------

total = reduce(lambda a, b: a + b, numbers_list)

print("Total using reduce:", total)


# -------------------------------
# Closure
# -------------------------------

def outer_function(message):
    def inner_function():
        print("Message:", message)
    return inner_function


my_closure = outer_function("Learning Python closures")
my_closure()


# -------------------------------
# Decorator
# -------------------------------

def simple_decorator(function):
    def wrapper():
        print("Before function execution")
        function()
        print("After function execution")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello, Python Decorators!")


say_hello()


# -------------------------------
# Operator Overloading
# -------------------------------

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


book1 = Book(100)
book2 = Book(150)

print("Total Pages:", book1 + book2)
