
import os

file_path = "/Users/yashnandankar/Library/Mobile Documents/com~apple~CloudDocs/Documents/python practice/file/text.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist.")

    if os.path.isfile(file_path):
        print("That is the file.")
    elif os.path.isdir(file_path):
        print("That is the directory")

else:
    print(f"The location dosen't exist.")