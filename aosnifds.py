"""
Module aosnifds
"""

def welcome_message():
    """Prints a welcome message."""
    print("Welcome to Tech Week Session")

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

if __name__ == "__main__":
    welcome_message()
    RESULT = add_numbers(5, 3)
    print(f"The result of adding 5 and 3 is: {RESULT}")
