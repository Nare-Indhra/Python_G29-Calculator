def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def exponentiate(a, b):
    return a ** b

def divide(a, b):
    if b !=0:
        return a / b
    else:
        raise ValueError("cannot divide by zero")
    
def calculator():
        num1 =float(input("input(Enter the first number :" ) )
        operation = input("Enter the operation (+, -,*, /)  ")
        num2 = float(input("Enter the second number : "))

        if operation == '+' :
            result =  add (num1,num2)
        elif operation == '-':
            result = subtract (num1,num2)
        elif operation == '*':
            result = multiply (num1,num2)
        elif operation == '/':
            result = divide(num1,num2)
        elif operation == '**':
            result = exponentiate(num1,num2)
        else:
            print(" Invalid operation")
        print(result)
calculator()