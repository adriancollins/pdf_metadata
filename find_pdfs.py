#find pdfs
import os
root_directory = './test_data/'
f = open('PDF_list.txt', 'w')
for root, dirs, files in os.walk(root_directory):
    for file in files:
        #f.write(os.path.join(root, file)+'\n')
        #print(os.path.join(root, file))
        file = file.lower()
        if file.endswith(".pdf"):
             print(os.path.join(root, file))
             #write to file
             f.write(os.path.join(root, file)+'\n')        
f.close()

print("fin")
