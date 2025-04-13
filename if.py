username=input("enter the username:")
password=input("enter the password:")
if username=="uday" and password=="sravya":
    print("welcome uday")
elif username=="uday" and password!="sravya":
    print("invalid user")
elif username!="uday" and password=="sravya":
    print("invalid user")
else:
    print("log in session closed")