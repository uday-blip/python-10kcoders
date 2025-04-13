#even or odd number
n=int(input("enter a number:"))
if n%2==0:
    print("given number is even ")
else:
    print("given number is odd")
#greater number in these two numbers
u=int(input("enter the  number u:"))
l=int(input("enter the  number l:"))
if u>l:
    print("u is the greater number")
elif l>u:
    print("l is the greater number")
else:
    print("both numbers are equal")
#whether the number is postive or negative   
n=int(input("enter a number:")) 
if n>0:
    print("the given number is positive")
elif n<0:
    print("the given number is negative")
else:
    print("the given number is zero")
#age verification for vote
v=int(input("enter your age:"))
if v>18:
    print("you can vote") 
else:
    print("you can't vote")
#student marks to decide pass or fail
n=int(input("enter your marks out of 100:"))
if 40<=n<=100:
    print("exam passed")
elif 0<=n<=40:
    print("exam failed")
else:
    ("enter valid marks")
    
Output :
    enter a number:4
given number is even 
enter the  number u:33
enter the  number l:44
l is the greater number
enter a number:-4
the given number is negative
enter your age:19
you can vote
enter your marks out of 100:55
exam passed

    
   