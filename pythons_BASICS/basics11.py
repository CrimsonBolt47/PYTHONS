user_input =input("enter name")
name = input("enter something")
message = "hello %s!!" % user_input #1st way
print(message)
message = f"hello {user_input}!!"  #2nd way (works only after 3.6 versions)
print(message)
message="hellp %s %s!!" % (user_input,name) #2 inputs 
print(message)
message=f"hello {userpeter_input} {name}," #2 inputs
print(message)
#space between %s %s and{} {} is important