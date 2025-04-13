nested=[
    [12,13,14,123,8],
    [15,16,-1,17],
    [18,108,19,20]
]
for i in range(len(nested)):
    print(i)
    sublist=nested[i]
    print(sublist)
    maximum_value=max(sublist)
    print(f'the max value of:',[i],"is",{maximum_value})
    minimum_value=min(sublist)
    print(f'the min value of:',[i],"is",{minimum_value})