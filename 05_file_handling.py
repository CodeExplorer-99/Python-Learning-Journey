# Day 5: File Handling and Exception Handling

def manage_file():
    filename = "day5_practice.txt"
    
    # 1. Writing to a file (फाईलमध्ये लिहिणे)
    print("--- Writing to file ---")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Hello! This is Day 5 of my Python Learning Journey.\n")
            file.write("Today I learned about File Handling and Exception Handling.\n")
        print(f"Success: Data written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

    # 2. Reading from a file (फाईल वाचणे)
    print("\n--- Reading from file ---")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")

    # 3. Exception Handling Example (एरर मॅनेजमेंट - Division by Zero)
    print("--- Exception Handling Demo ---")
    try:
        number = int(input("Enter a number to divide 100: "))
        result = 100 / number
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    except ValueError:
        print("Error: Please enter a valid integer number.")

if __name__ == "__main__":
    manage_file()
