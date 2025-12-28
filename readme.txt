{
 "name": "Yash",
 "age": 20,
 "job": "developer"
}{
 "name": "Yash",
 "age": 20,
 "job": "developer"
}import json
import csv

employees = {"name":"Yash",
             "age" : 20,
             "job":"developer"
             }

file_path = "readme.txt"
try:
    with open(file_path,"a") as file:
        json.dump(employees,file,indent=" ")
        print(f"json file '{file_path}' has been created ")

except FileExistsError:
    print("The file is already exist")