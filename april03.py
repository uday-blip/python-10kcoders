def primes(pr1,pr2,callback):#implemented callback in the parameters
    
    maximum=max(pr1,pr2)
    prime_start=2
    prime_count=0
    while prime_count<=maximum:
        
        is_primes=True
        for i in range(2,prime_start):
            if prime_start%i==0:
                
                is_primes=False
                break
        if is_primes==True:
            prime_count+=1
            if prime_count==pr1 or prime_count==pr2:
                callback(prime_start)
        prime_start+=1

def show_primes(primes):
    print(f'the primes found are',{primes})

pr1=int(input('enter a number:'))
pr2=int(input('enter a number:'))
primes(pr1,pr2,show_primes)





