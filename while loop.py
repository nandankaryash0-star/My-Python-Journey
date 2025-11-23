# while loop - if condition is true

name = input("Enter Your username:  ")

while name == "":
    print("You did not enter your username")
    name = input("Enter Your username:  ")

print(name)

age = int(input("Enter your age :  "))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter your age :  "))
print(f"hi {name} your age is {age} years old")