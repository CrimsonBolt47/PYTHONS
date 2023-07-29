array=[4.7,8.9,3.2,1.1]

for val in array:        #for loop
    print(round(val))     #inbuild func for rounding numbers
    print("yo")



dictt = {"yo": 2.5, "peter": 4.8, "hello": 6.1}
    
for val in dictt.items():  
        print(val)




name=""                            #normal for loop like c++
while name != "hello":            #method 1
    name=input("enter name")


while True:
    name=input("enter name:")    #method 2
    if name == "hello":
        break
    else:
        continue

