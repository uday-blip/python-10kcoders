'''citizen="indian"
age=19
if citizen=="african":
    if age>18:
        print("you are eligibel")
    else:
        print("age is not sufficent")
else:
    print("you are not eligible")'''

bill=10000
card="sbi"
if bill>=10000:
    if card=="sbi":
        print("you got 5% discount",bill*0.05)
    elif card=="hdfc":
        print("you got discount of 10%",bill*0.1)
    else:
        print("no discount for your card")
else:
    print("add more items worth ",10000-bill," to get discount")    