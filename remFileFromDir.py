#/usr/bin/python

import os
import sys

os.chdir(r"C:\Users\Desktop")
dir_content = os.listdir()
print("directory contents are: %s"%dir_content)
for file in dir_content:
    if file == "khvbh.docx":
        status=os.remove(file)
        if status:
            print("no file removed")
        else:
            print("file %s deleted successfully"%file)
    else:
        print("file not found")

            
print(sys.argv)


