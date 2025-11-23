print("New Beginig!")
print("Its really good")

first_name = "buddy"

print(first_name)
email = "yashnandankar2022@gmail.com"
food = "pizza"
print(f"I like {food}")
print(f"Your email is {email}")

#Integer
age = 19
print(f"my age is {age}")
quanity = 4
num_of_students = 85
print(f"i am buying {quanity} items")
print(f"my class have {num_of_students}")

#Float
price = 10.99
gpa = 3.9
distance = 1.5
print(f"The price is {price}")
print(f"my Gpa is {gpa}")
print(f"i ran {distance}")

#Boolean

is_student = False
for_sale = True

if for_sale:
    print("that item is for sale ") 
else:
    print("that itam is not for sale")     

#Type Casing = The process of convering a variablr data type to another

name = ""
age = 16
gpa = 3.6
is_student2 = True

gpa = int(gpa)
print(gpa)

#age = float(age)
print(age)

age = str(age)
print(age)

age += "1"
print(age)

name = bool(name)

print(name)

#inpu()= A function that prompts the use to enter data Returns the entered data as a string

name1 = input("What is your name?: ")
age1 = int(input("what is your age?: "))
age1 = age1 + 1

print(f"Hello {name1}!")
print("Happy Birthday")
print(f"you are {age1} years old")