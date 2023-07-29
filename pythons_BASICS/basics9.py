def mean(value):
    if type(value)==dict:
        hmean=sum(value.values())/len(value) #spaces is used intead of {}
    else:
        hmean=sum(value)/len(value)      #if isinstance(value,dict): is also same
                                         #isinstance checks datatype to the value   "isinstance(3,int)"    etc


return hmean


array=[3,5,6]
dic={"hello":5.7,"yo":3.1,"hey":9.5}
print(mean(array))
print(mean(dic))
