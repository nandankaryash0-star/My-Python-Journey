try:
    score = int(input("Enter your score(0-100): "))
    if 0<= score <=100:
        if score >=90:
            print("Grade is A")
        elif score >=80:
            print("Grade is B")
        elif score >=70:
            print("Grade is C")
        elif score >=60:
            print("Grade is D")
        else:
            print("Grade is F")
    else:
        print("Score must be between 0 and 100 ")

except ValueError:
    print("Please a valid number as score.")