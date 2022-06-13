# this script removes '- copia' tag from file names in a folder

import os
import re

folder = os.getcwd()

for file_name in os.listdir(folder):
    old_name = folder + "\\" +  file_name
    new_name = re.sub(r' - copia', '', old_name)

    os.rename(old_name, new_name)

print("All files renamed!")

print("New names are:")
result = os.listdir(folder)
print(result)

input()