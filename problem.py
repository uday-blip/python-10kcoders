num=12345
is_des=True
prev=num%10
while num!=0:
    last=num%10
    if prev<last:
        is_des=False
        break
    prev=last
    num=num//10
if is_des==True:
    print('is in descending order')
else: 
    print('is not in descending order')

num=934653371
my=3
count=0
length=0
place=[]
three=False
temp=num

while num!=0:
    num=num//10
    length+=1
print(length)
while temp>0:
    last=temp%10
    if last==my:
        three=True
        place.append(length)
        count+=1
    length-=1
    temp=temp//10
if three==True:
    print(place)
    print(count)
else:
    print('it do not exist')
        

