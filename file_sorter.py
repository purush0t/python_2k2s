import os
import re
import shutil
import sys
#folder path to execute the program
wrk_path = "path/to/the/folder/where/you/want/to/sort/the/files"

#changin current working directory
os.chdir(wrk_path)

# file_names = os.listdir()

print(os.system("DIR"))

# filtering out only the files, exculding folder and other stuff
f_names = [name for name in os.listdir() if os.path.isfile(name)]

# removing item's that start with "."
f_names = [x for x in f_names if not x.startswith(".")]
ext = list()

#extracting the extension of all the files
for r in f_names:
    ext.append(r.split(".")[1])
#removing duplicate extension
ext = list(set(ext))

#making directories in name of extension
for g in ext:
    print(f"making directory name:{g}")
    # handling the exception file exists 
    try:
        os.mkdir(g)
    except FileExistsError:
        print(f"folder>{g}: already exists!")
        #checks if the folder has  contents
        if len(os.listdir(g))==0:
            continue
        #exits program if the folder has contents
        else:
            print(f"folder:{g} has contents")
            print("exiting program...")
            sys.exit(0)

for r_n in f_names:
    for ex_t in ext:
        if r_n.split(".")[1] == ex_t:
            print("moving {} to {}".format(r_n,os.getcwd()+"\\{}".format(ex_t)))
            shutil.move(os.getcwd()+"\\{}".format(r_n),os.getcwd()+"\\{}".format(ex_t))
        else:
            continue

print("everthing is done eh!")

