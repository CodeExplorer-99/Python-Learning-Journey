# Day 1: Python Basics

# Python Introduction
print("Hello, Python!")

# Variables and Data Types
name = "Shubham"
age = 25
height = 5.8
is_learning = True

print(name)
print(age)
print(height)
print(is_learning)

# Checking Data Types
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))

# Built-in Functions
message = "python learning journey"

print(len(message))
print(message.capitalize())
print(message.upper())
print(message.lower())

# String Methods
text = "I am learning Python"

print(text.replace("Python", "Programming"))
print(text.split())

# Indexing
word = "Python"

print(word[0])
print(word[-1])

# Boolean and Comparison Operators
a = 10
b = 20

print(a < b)
print(a > b)
print(a == b)
print(a != b)

# Logical Operators
print(a < b and b > 15)
print(a > b or b > 15)
print(not(a > b))

# If Else Condition
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
