num=9346522711
prime=[]
while num!=0:
    last=num%10
    if last==2 or last==3 or last==5 or last==7:
        prime.append(last)
    num=num//10
print(prime)
        
    