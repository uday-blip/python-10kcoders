'''in python execption handling is also called as error handling methods the below are the some of the execption handling methods in python'''
'''1.try : it attempts to execute a block of Code   
execpt: it catches any errors and executes the code when try fails
else: it onely executes when there are no execptions
finally: this block executes no matter whether  our code is executed successfully or not '''
try:
    uday=[1,2,3]
    print(uday[4])
except Exception as error:
    print('not available:',error)
    
try:
    sum=10/1
except Exception as error:
    print('failed :',error) 
else:
    print(sum)   

try:
    u1='uday'
    u2=143
    v=u1+u2
except Exception as error:
    print('cannot do:',error)
else:
    print(v)
finally:
    print('this code is executed')

'''formated string: It can be created by giving f infront of statement that we want to print and we have to put a placeholder of the variable name in {} '''
'''method 2: .format it will use .format to insert variables in the print statement '''

s1=20
s2=25
p=s1+s2
print(f'the sum of both s1 and s2:',{p})
#.()format method.
name='usha'
age=21
print('my name is {} and iam {} years old.'.format(name,age))

#problem solving
uc='usha'
vowels='AEIOUaeiou'
new=""
for i in uc:
    if i in vowels:
        a_v=ord(i)
        n_c=chr(a_v+1)
        new=new+n_c
    else:
        new+=i
print(new)

#anagram
a='eleven plus two'
b='twelve plus one'
if len(a)!=len(b):
    print('it is not an anagram')
else:
    anagram=True
    for i in b:
        if b.count(i)!=a.count(i):
            anagram=False
            break
if anagram==True:
    print('it is an anagram')
else:
    print('it is not an anagram,')

#method 2

s1='polo'
s2='loop'
if len(s1)!=len(s2):
    print('not anagram')
else:
    anagram=False
    count=0
    for i in s2:
        if s2.count(i)==s1.count(i):
            count+=1
            if count==len(s1):
                anagram=True
if anagram==True:
    print('it is an angram')
else:
    print('not an anagram')