"""
Modular Calculator Program
Internship Task 5 – Functions & Modular Programming
"""

def add(a, b=0):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b=0):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b=1):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Return the division of two numbers.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def get_numbers():
    """Take two numbers from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def show_menu():
    """Display calculator menu."""
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def calculator():
    """Main calculator logic."""
    while True:
        show_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Exiting calculator...")
            break

        if choice in ["1", "2", "3", "4"]:
            a, b = get_numbers()

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        else:
            print("Invalid choice! Please try again.")


# Program execution starts here
if __name__ == "__main__":
    calculator()
