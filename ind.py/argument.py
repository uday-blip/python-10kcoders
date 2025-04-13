
str=input('enter a para:')
valid=True
for char in str:
    ascii=ord(char)
    if not(65<=ascii<=90 or 97<=ascii<=122) and not(char==' '):
        valid=False
        break
if valid==True:
    print('this is a valid paragraph')
else:
    print('this is a invalid paragraph')