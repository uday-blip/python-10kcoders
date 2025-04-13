# num=int(input("enter a number"))
# prime_not_found=True
# while prime_not_found:
#    fact=0
#    num+=1
#    for i in range(1,num+1,1):
#       if num%i==0:
#          fact+=1
#       if fact==2:
#          prime_not_found=False
#          print(num,"next prime")

nest=[[1,2,3],[4,5,6],[7,8,9]]
final=[]
for i in range(len(nest)):
   print(nest[i])
   for j in range(len(nest[i])):
      print(nest[i][j])
      final.append(nest[i][j])
print(final)