def weather(temp):                #if
    if temp >= 7:
        return "hot"
    
    elif temp<7 and temp>=3:  #else if
        return "warm"

    else:                     #else
        return "cold"


input1=input("enter value")    #input value is string

print(type(input1),input1)

input2=float(input("enter temperature")) #input value is converted to float

print(weather(input2))