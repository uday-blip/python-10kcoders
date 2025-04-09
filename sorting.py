digits=[1,2,3,4,5,6,5,4,3,2,1]
unq_items=[]
modified_unq=[]
for i in digits:
    if i not in unq_items:
        unq_items.append(i)
        modified_unq.append(i)
    else:
        modified_unq.append('*')
print(modified_unq)


num=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
print(even+odd)
print(f'the even numbers are:',(even),'and','odd numbers are:',(odd))