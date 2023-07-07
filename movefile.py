import os
import shutil

source1 = "moviefile.py"
destin = "C:\Users\RDxMANDRIN\Desktop"


list_of_files = os.listdir(source1)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    print(name)
    print(extension)