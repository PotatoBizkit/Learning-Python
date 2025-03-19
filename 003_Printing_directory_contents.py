import os

#mentioning the directory to list
path = "D:\\"

#Retrieve contents
contents = os.listdir(path)

#List contents
for i in contents:
    print(i)