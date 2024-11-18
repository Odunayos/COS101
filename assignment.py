# Define the functions for different physics/math operations
def operation_a():
    print("Function A: Addition")
    a, b = map(float, input("Enter two numbers separated by a space: ").split())
    print(f"The sum is: {a + b}")

def operation_b():
    print("Function B: Subtraction")
    a, b = map(float, input("Enter two numbers separated by a space: ").split())
    print(f"The difference is: {a - b}")

def operation_c():
    print("Function C: Multiplication")
    a, b = map(float, input("Enter two numbers separated by a space: ").split())
    print(f"The product is: {a * b}")

def operation_d():
    print("Function D: Division")
    a, b = map(float, input("Enter two numbers separated by a space: ").split())
    if b != 0:
        print(f"The quotient is: {a / b}")
    else:
        print("Error: Division by zero")

def operation_e():
    print("Function E: Power")
    base, exponent = map(float, input("Enter the base and exponent separated by a space: ").split())
    print(f"The result is: {base ** exponent}")

# Map user input to functions
operations = {
    'a': operation_a,
    'b': operation_b,
    'c': operation_c,
    'd': operation_d,
    'e': operation_e
}

# Main loop
while True:
    print("\nChoose an operation: A, B, C, D, E (or type 'exit' to quit)")
    user_choice = input("Enter your choice: ").lower()
    if user_choice == 'exit':
        print("Exiting the program. Goodbye!")
        break
    elif user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid choice, please try again.")