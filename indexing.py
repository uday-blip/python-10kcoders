n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
n3=int(input('enter a number:'))
big=max(n1,n2,n3)
small=min(n1,n2,n3)
print(big,small)
if big%n1==0 and big%n2==0 and big%n3==0:
    print(f'the lcm is:',{big})
else:
    temp=big
    while True:
        if temp%n1==0 and temp%n2==0 and temp%n3==0:
            print(f'the lcm of',{n1},{n2},{n3},"is",{temp})
            break
        temp+=big
    
