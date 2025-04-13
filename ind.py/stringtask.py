para="This Python code takes a string udayBABU and swaps each character's case, converting uppercase to lowercase and vice versa. It initializes an empty string new, loops through each character, checks its case using isupper(), and appends the swapped case version. The final output is UDAYbabu. The unused count variable is redundant but harmless. The code effectively demonstrates case conversion through iteration and string methods"
para=para.split(" ")

n_para=len(para)
print(n_para)
if n_para>50:
        print("the para is valid:")
else:
    print("the para is invalid:")
#task 2
name="UdAykiRAn"
count1=0
count2=0
for i in name:
    a=ord(i)
    if 65<=a<=90:
        count1+=1
    if 97<=a<=122:
        count2+=1
print("the upper case letter are:",{count1})
print("the lower case letters are:",{count2})
    