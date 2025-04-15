#local scope
def mine():
    x='uday'
    print(x) #can be used here cause it is local scope
mine()
# print(x) '''throws an error cause it is not avaiable outside the scope'''

#Enclosing scope 
#keyword = nonlocal
def outer():
    count=100 #Variable in Enclosed scope
    
    def inner():
         nonlocal count #Creating access to variable by using nonlocal keyword.
         count+=15 #accessed and modified the nonlocal variable.
    inner()
    print(count) #printing output of modified count
outer()
#print(count) would raise an error

#global Scope
#keyword = global
u=' udhay ' #global variables u,k,d
k='kiran'
d='doddavarapu'
def my_name():
    global u,d #accessing the global variables by giving global keyword.
    u+=k 
    d+=u
#here we didn't mentioned global 'k' because we ain't modifying that variable k
my_name()
print(u)
print(d)
    
#built-in scope 
#no keyword required
#built-in function len is available
print(len('apple')) #output is 5
#overridding the built-in function here
len=10
print(len) #output is 10
#again restoring the orginal built-in len function 
del len
a='banana'
print(len(a)) #output is 6

#finding max and second max values in a list
list=[1,2,3,4,5,2,1,32,45,32]
max=list[0]
sec_max=list[1]
for i in range (len(list)):
    if list[i]>max and list[i]>sec_max:
        sec_max=max
        max=list[i]
    if list[i]<max and list[i]>sec_max:
        sec_max=list[i]
print(max,sec_max)