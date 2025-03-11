import datetime


# Function to display the current date and time
def display_datetime():
    now = datetime.datetime.now()
    print("Current date and time:", now)

# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the enhanced Python app.")

# Function to perform a simple calculation
def perform_calculation():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")

