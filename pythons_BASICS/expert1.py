myfile=open("fruits.txt")   #files
print(myfile.read())        #when executed 1st time cursor reaches from starting to the end so second time it is printed it only prints empty string
#because cursor goes from end to end
print(myfile.read())
print(myfile.read())

myfile.close()          #closing file (optional)

print("##########")
myfi=open("fruits.txt")
hey=myfi.read()
print(hey)
print(hey)
print(hey)

myfi.close()      #closing file

with open("fruits.txt") as myfiless:   #another way to open file 
    content=myfiless.read()             #this automatically also closes the file so no need of .close()

print(content)