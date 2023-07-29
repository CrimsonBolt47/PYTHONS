with open("vegetables.txt","a+") as myfile: #"a"is for appending but it can only be used for writing 
    #therfore "+"is used for doing both reading and writing
    myfile.write("\nonion")                  #
    myfile.seek(0)                          #after reading it goes to end of file so use seek() to go to the beginning
    content=myfile.read()
print(content)