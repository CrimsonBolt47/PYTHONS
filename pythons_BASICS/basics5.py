listt=[1,2,3,4,5] #list functions
listt.append(6)
listt.remove(2)
print(listt)
print(listt.__getitem__(1))  #1 is index
list2=[7,9,10.5]
listt.append(list2[2])
print(listt)
print(listt[2:4])  #get only a portion of an array from 2 to 3 (4th index not printed)
print(listt[-2:])  #  (-) index indicates opposite side of array
#from the opposite it starts from -1 ex listt=[-5,-4,-3,-2,-1]==listt[0,1,2,3,4]
print(listt[:3])  #this prints values before 3 index(3rd index is not printed)