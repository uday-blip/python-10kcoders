#function to add numbers .
# def add(a,b):
#     c=a+b
#     print(c)  
# add(12,14)
# #function to greet someone.
# def greet(name):
#     print("hello good morning"+name)
# greet("uday")
# #function to square number .
# def square(num):
#     num=num**2
#     print(num)
# square(12)
# #function to multiply  numbers .
# def mul(a,b):
#     c=a*b
#     print(c)
# mul(12,3)
# #function to find length of a string .
# def lengt(a):
#     print(len(a))
# lengt("udhay")

# Output:
#     26
# hello good morninguday
# 144
# 36
# 5

def combined_function(operation, *args):
    if operation == "add":
        result = args[0] + args[1]
        print(f"Addition: {result}")
    
    elif operation == "greet":
        name = args[0]
        print(f"Hello, good morning {name}!")
    
    elif operation == "square":
        num = args[0]
        squared = num ** 2
        print(f"Square: {squared}")
    
    elif operation == "multiply":
        product = args[0] * args[1]
        print(f"Multiplication: {product}")
    
    elif operation == "length":
        string = args[0]
        print(f"Length: {len(string)}")
    
    else:
        print("Invalid operation!")
combined_function(15,4)