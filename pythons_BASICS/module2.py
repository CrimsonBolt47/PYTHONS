import time              #it is inbuilt module imported
import os   
import pandas             #standard module (inside python file)

while True:
    if os.path.exists("temp.csv"):
       data=pandas.read_csv("temp.csv")
       print(data.mean())
    else:
        print("file doesnt exist")
    time.sleep(5)   