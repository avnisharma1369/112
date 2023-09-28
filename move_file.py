import os 
import shutil
from_dir="/Users/sunilsharma/Desktop/projects/download_Files"
to_dir="/Users/sunilsharma/Desktop/projects/document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for fileName in list_of_files:
    name,extension=os.path.splittext(fileName)
    if extension=='':
        continue
    if extension in ['.txt','jpg']:
        path1=from_dir+'/'+fileName
        path2=to_dir+'/'+fileName
        path3=to_dir+ '/' + "Document_Files" + '/' + fileName
        if os.path.exists(path2):
            print("moving"+ fileName + ".....")
            shutil.move(path1,path3)
        else:
             os.mkdir(path2)
             print("moving"+fileName+".....")
             shutil.move(path1,path3)