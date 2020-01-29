def printPascal(n):
   for line in range(1,n+1):
    A=1
   for i in range(1,line+1):
       print(A)
       A=A*(line-1)/i
       print ("\n")
n=int(input("enter the value:"))    
printPascal(n)
