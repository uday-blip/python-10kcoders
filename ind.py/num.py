#print the prime numbers in the following number
num=9346522711
prime=[]
while num!=0:
    last=num%10
    if last==2 or last==3 or last==5 or last==7:
        prime.append(last)
    num=num//10
print(prime)

#armstrong numbers
num=9474
length=0
temp=num
temp2=num
while num!=0:
    num=num//10
    length+=1
print(length)
total_sum=0
while temp!=0:
    last=temp%10
    total_sum=total_sum+last**length
    temp=temp//10
print(total_sum==temp2)

    
        
    
