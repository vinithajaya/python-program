import random
a=random.randrange(1,200)
a1=int(input("enter the number:"))
if a1==a:
    print("guessing number is correct")
elif a1<a:
    print("guessing number is less")
else:
    print("guessing number is greater")
