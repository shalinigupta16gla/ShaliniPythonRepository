#/usr/bin/python
#to remove file from dir

import os
import sys
import time
import copy

print(time.ctime(time.time()))
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


