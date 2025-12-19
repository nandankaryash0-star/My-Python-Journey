#Share among all instance of classes , Defined outside the constructor , Allow u to share data among all object created from that class

class student:

    class_year = 2026
    num_students = 0

    def __init__(self,name,age,classs,roll):
        self.name = name
        self.age = age
        self.classs = classs
        self.roll = roll
        student.num_students += 1

student1 = student("Dogesh",5,"1st",70)
student2 = student("Mewo",2,"1st",34)
student3 = student("Cow",12,"2nd",1)


print(f"The total num of students graduating this year {student.class_year} is {student.num_students}")
print(f"The name of student is {student1.name}")
print(f"The name of student is {student2.name}")
print(f"The name of student is {student3.name}")

