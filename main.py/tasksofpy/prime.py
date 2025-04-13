# # # digit=int(input('enter a number:'))
# # # prev_prime_not_found=True
# # # while prev_prime_not_found==True:
# # #     fact=0
# # #     digit-=1
# # #     for i in range(2,digit):
# # #         if digit%i==0:
# # #             fact+=1
# # #             break
# # #     if fact==0:
# # #         print('the previous prime number is:',{digit})
# # #         prev_prime_not_found=False
    
    
    
    
# # dig=int(input('enter a number:'))
# # length=0
# # temp=dig
# # temp2=dig
# # while dig !=0:
# #     dig=dig//10
# #     length+=1
# # print(length)
# # total_sum=0
# # while temp !=0:
# #     last=temp%10
# #     total_sum=total_sum+last**length
# #     temp=temp//10
# # print(total_sum == temp2)
    
# a1="polo"
# a2="loop" 
# if len(a1)!=len(a2):
#     print('not anagram')
# else:
#     anagram=True
#     for i in a2:
#         if a2.count(i)!=a1.count(i):
#             anagram=False
#             break
# if anagram==True:
#     print('anagram')
# else:
#     pirnt('not anagram')



a=3
b=2.0
c=a+b
print(c)
print(type(c))