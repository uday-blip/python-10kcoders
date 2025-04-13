  
 #printing the count of values of a key 
my_dict={
    "name":"udhay",
    "languages":"telugu,hindi,english",
    "skills":"Frontend,backend,database,aws,aiml"
}
print(my_dict)
print(len(my_dict))
print(my_dict.get("skills"))
skill_list=my_dict.get("skills").split(",")
print(len(skill_list))

  #printing prime and non prime numbers of a list  


num=[1,2,3,4,5,6,7,8,9,10]
prime=[]
non_prime=[]
for i in range(0,len(num),1):
    fact=0
    number=num[i]
    for k in range(1,number+1,1):
        if number%k==0:
            fact+=1
    if fact==2:
        prime.append(number)
    if fact>2:
        non_prime.append(number)
print(prime)
print(non_prime)
output:

[2, 3, 5, 7]
[4, 6, 8, 9, 10]
