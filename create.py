import os

folder_name = "my_folder"
file_name = "notes.txt"

# 1. Create the folder (exist_ok=True ensures it won't crash if the folder already exists)
os.makedirs(folder_name, exist_ok=True)

# 2. Combine the folder and file name safely across different operating systems
file_path = os.path.join(folder_name, file_name)

# 3. Create and write text into the file
with open(file_path, "w") as file:
    file.write("Hello! This text is inside a file inside a folder.")

print(f"Successfully created: {file_path}")
