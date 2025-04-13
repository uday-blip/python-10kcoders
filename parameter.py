# # # print('hello')
# # # def mul_numbers():
# # #     n1=int(input("enter a number"))
# # #     n2=int(input("enter a number"))
# # #     return n1*n2
# # # print(mul_numbers()

# # mul=lambda u=int(input('enter a number1:')),v=int(input('enter a number')):u*v
# # # print(mul())

# def div(n1,n2):
#     return n1/n2

# def mul_2(m):
#     print(m)
#     return m*2

# print(mul_2(div(15,3)))


def login():
    username=input('enter username :')
    password=input('enter password :')
    
    if username=="uday" and password=="harry":
        return True
    else:
        return False

def show_data():
    if login():
        print("welcome back")
    else:
        print('pls login! ')
show_data()
