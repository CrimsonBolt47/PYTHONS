import time              #it is inbuilt module imported
import os                #standard module (inside python file)

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())
    else:
        print("file doesnt exist")
    time.sleep(5)   
     

#to chech imported modules
 #import sys                      #check in python shell
 #sys.builtin_module_names
 #then import the modules         #know more from dir()