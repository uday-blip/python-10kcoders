def loan():
 n=input("enter your name:")
 g=input("enter your gender:")
 a=int(input("enter your age:"))
 if 18<=a<=58:
       print("you can go for the next step")
 else:
     print("no loan is offered for you")
     return
 s=int(input("enter your annual income:"))
 if s>=350000:
     print("you can proceed to cibil score checking")
 else:
     print("you can't proceed further")
     return
 c=int(input("enter your cibil score:"))
 pl=s*0.40
 ml=s*0.60
 ul=s*0.80
 hl=s*0.90
 bl=s*1.2
 sl=s*0.70
 cl=s*0.75
 uhl=s*1.0
 if 18<=a<=45 and 350000<=s<=800000 and 300<=c<=650:
     print("your loan amount is " ,pl,"to",ml)
 elif 18<=a<=45 and 800000<=s<=1500000 and 300<=c<=650 :
     print("your loan amount is ",pl , "to",ul)
 elif 18<=a<=45 and 800000<=s<=1500000 and c>650:
     print("your loan amount is ",pl ,"to",hl)
     
 elif  18<=a<=45 and s>1500000 and 300<=c<=650:
     print("your loan amount is",pl,"to",hl)
 elif 18<=a<=45 and s>1500000 and c>650:
     print("your loan amount is ",pl,"to",uhl)

 elif 46<=a<=58 and 350000<=s<=800000 and 300<=c<=650:
     print("your loan amount is",pl,"to",sl)
 elif 46<=a<=58 and 350000<=s<=800000 and c>650:
     print("your loan amount is",pl,"to",cl)
 elif 46<=a<=58 and 800000<=s<=1500000 and 300<=c<=650:
     print("your loan amount is",pl,"to",ul)
 elif 46<=a<=58 and 800000<=s<=1500000 and c>650:
     print("your loan amount is",pl,"to",ul)
 elif 46<=a<=58 and s>1500000 and 300<=c<=650:
     print("your loan amount is ",pl,"to",sl)
 elif 46<=a<=58 and s>1500000 and c>650:
     print("your loan amount is",pl,"to",sl)
 else:
     print("no loans at this moment")
loan()
    
    

    
    
