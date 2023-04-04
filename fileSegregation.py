import os
import shutil

from_dir ="C:/Users/Suraj P/Downloads"
to_dir="D:/Awdesh/"
list_of_files = os.listdir(from_dir)
#ext1=[ .txt', .doc', .docx', .pdf'']

#print(list_of_files)

#for var in list_of_files
for file in list_of_files:
    name,ext = os.path.splitext(file)
    if ext==" " :
        continue
    if ext in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir+'/'+file  #"C:/Users/Suraj P/Downloads/file"
        path2 =  to_dir + '/' + "Document_Files" #"D:/Awdesh/Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file  #D:/Awdesh/Document_Files/files

        if os.path.exists(path2):
            print("Moving " + file + ".....")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)    
            print("Moving " + file + ".....")
            shutil.move(path1,path3)