def addition(x,y):
    z = x + y
    print(z)

def substraction(x,y):
    z = x - y
    print(z)

def multiply(x,y):
    z = x * y
    print(z)

def divide(x,y):
    z = x / y
    print(z)



a = input("Enter the math problem: ")

if a == "addition":
    x = int(input("num1: "))
    y = int(input("num2: "))
    print(addition(x,y))

elif a == "substraction":
    x = int(input("num1: "))
    y = int(input("num2: "))
    print(substraction(x,y))

elif a == "divide":
    x = int(input("num1: "))
    y = int(input("num2: "))
    print(divide(x,y))

elif a == "multiply":
    x = int(input("num1: "))
    y = int(input("num2: "))
    print(multiply(x,y))

else:
    print("Enter correct operations ")

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

create_name("yash","nandankar")