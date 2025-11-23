#if = Do some code IF some condition is True else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old ")
elif age < 0:
    print("You havent been born Yet!")
elif age >=18:
    print("You are eligible ") 
else:
    print("You must be 18 +")    