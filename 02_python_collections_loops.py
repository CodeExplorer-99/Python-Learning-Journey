# Day 2: Python Collections and Loops

# -------------------------------
# Python Lists
# -------------------------------

fruits = ["apple", "banana", "mango"]

print("Original List:", fruits)

# append() - Adds one element at the end
fruits.append("orange")
print("After append:", fruits)

# extend() - Adds multiple elements
fruits.extend(["grapes", "pineapple"])
print("After extend:", fruits)

# insert() - Adds element at specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# remove() - Removes specific element
fruits.remove("banana")
print("After remove:", fruits)

# pop() - Removes element using index
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("After pop:", fruits)

# sort() - Sorts list
fruits.sort()
print("After sort:", fruits)

# reverse() - Reverses list
fruits.reverse()
print("After reverse:", fruits)


# -------------------------------
# Python Tuples
# -------------------------------

numbers = (10, 20, 30, 40)

print("Tuple:", numbers)
print("First value:", numbers[0])
print("Last value:", numbers[-1])


# -------------------------------
# Python Sets
# -------------------------------

unique_numbers = {1, 2, 3, 4, 4, 5}

print("Set:", unique_numbers)

unique_numbers.add(6)
print("After add:", unique_numbers)

unique_numbers.remove(3)
print("After remove:", unique_numbers)

# discard() does not give error if element is not present
unique_numbers.discard(10)
print("After discard:", unique_numbers)


# -------------------------------
# Python Dictionaries
# -------------------------------

student = {
    "name": "Shubham",
    "age": 25,
    "course": "Python"
}

print("Dictionary:", student)
print("Student Name:", student["name"])
print("Course:", student["course"])

# Updating dictionary value
student["course"] = "Python Programming"
print("Updated Dictionary:", student)

# Adding new key-value pair
student["city"] = "Gandhinagar"
print("After adding city:", student)


# -------------------------------
# While Loop
# -------------------------------

count = 1

while count <= 5:
    print("While Loop Count:", count)
    count += 1


# -------------------------------
# For Loop
# -------------------------------

for fruit in fruits:
    print("Fruit:", fruit)


# -------------------------------
# Break Statement
# -------------------------------

for number in range(1, 10):
    if number == 5:
        break
    print("Break Example:", number)


# -------------------------------
# Continue Statement
# -------------------------------

for number in range(1, 6):
    if number == 3:
        continue
    print("Continue Example:", number)
