#a simple Python exercise to revise basics

name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
    age1 = age + 10

    print(f"Hello {name}, you are {age} years old and will be {age1} in 10 years")

except ValueError:
    print("Please enter a valid number")