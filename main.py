from art import logo

print(logo)

""" Will add more operations as needed """

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

operations_dict = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": power}

def calculator():
    num1 = float(input("What's the first number?: "))
    
    for key in operations_dict:
        print(key)
    
    continue_check = True
    while continue_check:
        operation_selection = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation = operations_dict[operation_selection]
        answer = calculation(num1, num2)
    
        print(f"{num1} {operation_selection} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation ") == "y":
            num1 = answer
    
        else:
            continue_check = False
            calculator()

calculator()