import json
from difflib import get_close_matches


data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("did you mean %s instead ?"% get_close_matches(w,data.keys())[0])
        if yn=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'n':
            return "word doesnt exist then"
        else:
            return "respond properly"
    else:
        return "word doesnt exist"


word =""

while word !="/end":
    word =input("enter word: ")
    if word !="/end":
        output =translate(word)

        if type(output)==list: 
            for item in output:
                print(item)
        else:
            print(output)
    else:
        print("goodbye")
        exit()