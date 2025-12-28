
txt_data = "Hello their i am ghost an AI ML dev how may i help you."

file_path = "readme.txt"

with open(file_path,"w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' has been created ")