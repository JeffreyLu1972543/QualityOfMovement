import re
import os
data_path = '/Users/jeffreylu/Desktop/NTUdataset/subset'
for file_name in os.listdir(data_path):
    if file_name.endswith('.skeleton'):
        with open(os.path.join(data_path, file_name), "r") as file:
            content = file.read()
            match = re.search(r"\d+", content)
            if match:
                first_number = match.group()
                print(f"The first number in the file is: {first_number}")
            else:
                print("No number found in the file.")



folder_path = '/Users/jeffreylu/Desktop/NTUdataset/subset'  # replace with your folder path
file_count = 0

for _, _, files in os.walk(folder_path):
    file_count += len(files)

print(f"The folder {folder_path} contains {file_count} files.")