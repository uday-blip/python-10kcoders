#to find the missing digits in a number list
numbers=[1,3,4,5,7,8,9]
small=min(numbers)
big=max(numbers)
missing=[]
for i in range(small,big+1):
    if i not in numbers:
         missing.append(i)
print(f'the missing digits are:',(missing))

#to find the percetages of the given salaries in a dictionary


income={
    "uday":45000,
    "sai":60000,
    "vijay":80000
}
total_income=0
for key in income:
    total_income+=income[key]
print(total_income)
income['average_of_income_is']=total_income/len(income)
income['percent_of_uday']=round((income['uday']/total_income)*100,3)
income['percent_of_sai_is']=round((income['sai']/total_income)*100,3)
income['percent_of_vijay_is']=round((income['vijay']/total_income)*100,3)
print(income)