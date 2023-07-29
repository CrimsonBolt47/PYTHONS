temps = [441,583,816]

new1=[]                #normally done
for tem in temps:
    new1.append(tem/10)

print(new1)

new2=[tem/10 for tem in temps]        #dynamically done

print(new2)

tempss =[321,456,-999,395] #ignore -999

new_temp = [tem/10 for tem in tempss if tem !=-999]
print(new_temp)

new_temp = [tem/10 if tem !=-999 else 0 for tem in tempss]
print(new_temp)    #for if else ,if else must come before for loop