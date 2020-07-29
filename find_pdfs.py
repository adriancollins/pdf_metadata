#!/usr/bin/env python
import os
root_directory = '.\\test_data\\' #input your root directory
f = open('PDF_list.txt', 'w')
for root, dirs, files in os.walk(root_directory):
    for file in files:
        file = file.lower() #cleaning data for next matching step
        if file.endswith(".pdf"):
             print(os.path.join(root, file))
             #write to file
             f.write(os.path.join(root, file)+'\n')
f.close()

print("fin")
