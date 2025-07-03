#otp without zeroes
import random
otp=""
while len(otp)<6:
    digit=(random.randint(0,9))
    if digit!=0:
        otp+=str(digit)
print(f'your otp is {otp}')

#number picking game
numbers=[11,22,33,48]
print("you have got only 3 chances")
correct=(random.choice(numbers))
chances=0
for i in range(0,3,1):
    user_num=int(input("guess the correct number :"))
    if user_num==correct:
        print("you won !")
        break
    else:
        chances+=1
        if chances==3:
            print("you loss, better luck next time")

