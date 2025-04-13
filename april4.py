#to check the previous prime number
digit=int(input('enter a digit:'))
prev_prime_no=True
while prev_prime_no==True:
    fact=0
    digit-=1
    for i in range(2,digit):
        if digit%i==0:
            fact+=1
            break
    if fact==0:
        print('the previous prime number is:',{digit})
        prev_prime_no=False