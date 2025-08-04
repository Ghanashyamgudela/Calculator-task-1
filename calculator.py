# Operation functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    return a / b if b != 0 else "Error: Cannot divide by zero"

# Dictionary mapping operations
operations = {
    '1': ('Addition', add),
    '2': ('Subtraction', subtract),
    '3': ('Multiplication', multiply),
    '4': ('Division', divide)
}

# Function to handle the calculation
def perform_operation(choice):
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operation_name, operation_func = operations[choice]
        result = operation_func(x, y)
        print(f"{operation_name} result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Main loop
def run_calculator():
    while True:
        print("\n==== Simple Calculator ====")
        for key in operations:
            print(f"{key}. {operations[key][0]}")
        print("5. Exit")

        user_choice = input("Choose an option (1-5): ")

        if user_choice == '5':
            print("Thanks for using the calculator!")
            break
        elif user_choice in operations:
            perform_operation(user_choice)
        else:
            print("Invalid option. Please select 1-5.")

# Start of calculator program
run_calculator()
