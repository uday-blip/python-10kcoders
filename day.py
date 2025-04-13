username=input("enter the username:")
password=input("enter the password:")
if username=="username" and password=="password":
    print("welcome user")
elif username=="username" and password!="password":
    print("invalid user")
elif username!="username" and password=="password":
    print("invalid user")
else:
    print("invalid credintails")