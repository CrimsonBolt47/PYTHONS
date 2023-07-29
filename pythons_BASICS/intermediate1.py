def sentence(phrase):
    cap=phrase.capitalize()
    interrogative=("how","what","why")
    if phrase.startswith(interrogative):
        return "{}?".format(cap)

    else:
        return "{}.".format(cap)

result=[]
while True:
    inp=input("say something")
    if inp == "\end":
        break
    else:
        result.append(sentence(inp))

print(result)   #prints in list

print(" ".join(result))   #prints as a sentence