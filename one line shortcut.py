#Conditional expresion
# "X" if "Conditional" else "Y"

#num = float(int(input("Enter the Num..")))
#a = float((input("Enter the Num  a .. ")))
#b = float((input("Enter the Num  b .. ")))
age = 18
temp = 29
user_name = "Ysh"
#print ("Even" if num % 2 == 0 else "Odd" )

#print ("Positive" if num > 0 else "Negative")

#result = "Even" if num % 2 == 0 else "Odd"

#max_num = a if a>b else b
#min_num = a if a<b else b

status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temp >=30 else "Cold"
acces = "acces granted" if user_name ==  "Yash" else "acces denied"

print(acces)