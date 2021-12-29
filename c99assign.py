import os
import shutil
import time

path=input("enter the path of the folder: ")
path=path +'/'
days=int(input("enter the number of days: "))
seconds=time.time()-(days*24*60*60)
list_Of_Files= os.listdir(path)

exists=os.path.exists(path)

for file in list_Of_Files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    print(ext)
    if exists:
        new_path=os.path.join(path + file)
        print(new_path)
        st_ctime=os.stat(new_path).st_ctime
        print(st_ctime)

        if st_ctime<=seconds:
            if ext=='':
                shutil.rmtree()
            else:
                os.remove(path)
    else:
        print("path doesnot exists")



