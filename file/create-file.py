import csv

coustomer = [["Name","Age","Product"],
             ["Yash",20,"Mac M4"],
             ["Vedanti",19,"Mac M4"],
             ["Dogesh",23,"Mac pro M4"]]

file_path = "coustomer.csv"

with open(file_path,"w") as file:
    writer = csv.writer(coustomer,file)
    print(f"The csv file has been created {file_path}")