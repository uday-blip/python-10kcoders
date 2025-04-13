num = int(input("Enter an integer: "))
shift = int(input("Enter the number of positions to shift right: "))
result = num >> shift
print(f"The result of {num} >> {shift} is: {result}")

Output:
    Enter an integer: 16
Enter the number of positions to shift right: 2
The result of 16 >> 2 is: 4