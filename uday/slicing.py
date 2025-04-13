nest_list=[
    [1,2,3],
    [34,56,44],
    [77,88,32,-1]
]
for i in range(len(nest_list)):
    print(i)
    sublist=nest_list[i]
    print(sublist)
    max_val=max(sublist)
    print(f'the maximum value is:',{max_val})
    min_val=min(sublist)
    print(f'the minimum value is :',{min_val})