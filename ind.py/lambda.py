def combined_functions(a,b,operation):
    if operation=="add":
        result=a+b
        print(f'the addition is:{result}')
        return result
    elif operation=="sub":
        minus=a-b
        print(f'the subtraction is:{minus}')
        return minus
    elif operation=="mul":
        into=a*b
        print(f'the multiplication is:{into}')
        return into
    elif operation=="div":
        by=a/b
        print(f'the division is:{by}')
        return by
    elif operation=="modulus":
        remainder=a%b
        print(f'the modulus division is:{remainder}')
        return remainder
    elif operation=="floor division":
        float=a//b
        print(f'the floor division is :{float}')
        return float
    else:
        print(f'the operations is invalid ')
combined_functions(15,4,"add")
combined_functions(15,4,'sub')
combined_functions(15,4,'mul')
combined_functions(15,4,'div')
combined_functions(15,4,'modulus')
combined_functions(15,4,'floor division')   

#lambda functions for mathematical functions  
addition=lambda a,b:a+b
print(addition(15,4))
subtraction=lambda a,b:a-b
print(subtraction(15,4))
multi=lambda a,b:a*b
print(multi(15,4))
division=lambda a,b:a/b
print(division(15,4))
modulus=lambda a,b:a%b
print(modulus(15,4))
floordiv=lambda a,b:a//b
print(floordiv(15,4))