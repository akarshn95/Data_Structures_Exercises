import os

def find_files(suffix,path):
    items=os.listdir(path)

    for i in items:
        file=os.path.join(path,i)
        if os.path.isfile(file):
            if file.endswith(suffix):
                print(file)
        if os.path.isdir(file):
            find_files(suffix,file)
    
    return 

print("TEST CASE 1\n")
path=os.path.join(os.getcwd(),"testdir")        #path containing 4 files with suffix .c
find_files(".c",path)
print("TEST CASE 2\n")
path=os.path.join(os.getcwd(),"testdir2")      #empty folder, edge case, prints nothing
find_files(".txt",path)
print("TEST CASE 3\n")
path=os.path.join(os.getcwd(),"testdir3")      #folder containing 4 files with suffix .py
find_files(".py",path)
