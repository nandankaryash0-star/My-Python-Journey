#One line shortcut
# if x else y 
num = -5
age = 14
temperature = 40
user_role = "admin"

print("possitive" if num >0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

#max_num = a if a>b else b
#min_num = a if a<b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT " if temperature > 20 else "COLD"
access_level = "Full Access" if user_role =="admin" else "access limited"


print(access_level)