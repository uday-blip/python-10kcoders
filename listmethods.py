a=[1,2,3,4,5]
c=[]
for i in range(1,6,1):
    c.append(i)
print(c)
Output:
    [1, 2, 3, 4, 5]


g=[1,2,2,3,4,5,5,6,7,]
num=int(input("enter a number"))
count=0
for j in range(0,len(g),1):
    if g[j]==num:
        count+=1
print(count)
Output:
    enter a number 5
2