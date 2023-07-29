with open("vegetables.txt","w") as myfile:      #"w" is for writing "r" is for reading but "r" is optional
    myfile.write("tomato")

with open("fruits.txt","w") as myfil:
    myfil.write("\ngarlic\npear")         #writing is overwritten over the file