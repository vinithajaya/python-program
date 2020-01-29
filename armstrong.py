a=(input("Enter the value:"))
sum = 0
for i in a:
    b=int(i)+int(i)+int(i)
    sum=sum+b
if(a==sum):
    print("is armstrong number")
else:
    print("is not armstrong number")   
