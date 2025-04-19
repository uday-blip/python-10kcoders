#to print the count of fibinocii numbers in the range of 0 to 500 
limit=500
a=0
b=1
count=0
while a<=limit:
    print(a)
    count+=1
    c=a+b
    a=b
    b=c
print(f'the count of fibinoci numbers that are in',{limit} ,'range are',{count})