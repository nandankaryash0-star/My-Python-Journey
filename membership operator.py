#word = "MANGO"

#letter = input("Guess a letter in the secreat word: ").upper()

#if letter in word:
#    print(f"There is a {letter}")

#else:
#    print(f"{letter} was not found")

    # in and not in are the membership operator


grade = {"Spiderman":"A",
         "Iron man":"A+",
         "Starlord":"C",
         "Thor":"B"}

student = input("Enter the name of student: ")

if student in grade:
    print (f"{student}'s Grade is {grade[student]}")

else:
    print (f"{student} was not found")
