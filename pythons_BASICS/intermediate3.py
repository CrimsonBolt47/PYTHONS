def mean(*args):         #   * can take many variables as arguements   and returns them  as tuple
    return args          

def meann(**kargs):     # ** takes  many arguements and returns them  as dictionary
    return kargs

print(mean(1,2,3,4,5))          #this is non keyworg arguements--tuples list etc


print(meann(a=1,b=5,c=9))     #this is keyword arguements