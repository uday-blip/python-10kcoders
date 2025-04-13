num=[2,3,5,6,7,10]
if num[0]%2==0 and num[5]%2==0:
  print("True")
else:
    print("False")
    
    

def cnt(num):
    k=[8,9,2,2,4,3,5,5,9,1]
    count=0
    for i in range(0,len(k),1):
        if k[i]==num:
            count+=1
    print(count)
cnt(5)



j=[2,3,4,7,11,8,13]
d=[]
for i in range(0,len(j),1):
    fact=0
    for k in range(1,j[i]+1,1):
        if j[i]%k==0:
            fact+=1
    if fact==2:
        d.append(j[i])
print(d) 

