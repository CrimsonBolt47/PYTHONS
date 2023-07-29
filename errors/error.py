def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "dont divide by 0 yo"

print(divide(1,2))

print(divide(1,0))

