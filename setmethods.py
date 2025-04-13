#print the following set by removing only 7 from it 
alpha={1,2,3,4,5,6,7,8,9,10}
u=set({})
print(type(u))
for i in alpha:
    if i!=7:
        u.add(i)
print(u)

#output
<class 'set'>
{1, 2, 3, 4, 5, 6, 8, 9, 10}

#implementing the frozen set methods on a set
u={1,2,3,4,5}
v={5,4,3,2,1}
print(v.isdisjoint(u))
print(v.issubset(u))
print(v.issuperset(u))

#output:
False
True
True
