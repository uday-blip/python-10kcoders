#to verify a list of users in a dictionary and letting them vote.
details=[{
    "name":"uday",
    "age":19,
    "citizenship":"indian"},
         {
    "name":"akhil",
    "age":18,
    "citizenship":"russian"
}]
#we have created a list of dictionaries
for i in range(len(details)):                   #iteration over the items
    if details[i]["age"]>18:
        if details[i]["citizenship"]=="indian": #checking both if conditions will match or not
            details[i]["eligible"]=True         #printing eligible if both conditions are true
            print(details[i]["name"],"you can vote")
    else:
        details[i]["eligible"]=False           #printing not eligible if the conditons are false
        print(details[i]["name"],"wait for some time")   
print(details)


#consider a tuple and printing all the unique items of that tuple in a new list
mr_uday=(1,2,3,2,"hi",4,5,"hello",5,7,9,"uday")
new_list=[]                  #created a new list to print unique items
print(type(mr_uday))
for i in mr_uday:            #to iterate i in each element of mr_uday
    count=0                  #intilizise a variable count=0 for later use
    for j in mr_uday:        #iterating j in each element of i
        if i==j:             #if elements in i = j
            count+=1   
    if count==1:             #after incrementation the count =1
        new_list.append(i)   #adding unique elements through append method
print(new_list)
print(mr_uday)

