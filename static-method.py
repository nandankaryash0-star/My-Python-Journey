
class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_position
    
employee1 = Employee("Yash N","NLP Manager")
employee2 = Employee("Sanika","Manager Assisstance")
employee3 = Employee("mewo mewo","DS enginner")

print(Employee.is_valid_position("Cook"))
print(employee2.get_info())