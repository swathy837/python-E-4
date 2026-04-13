def factorail(num):
    if num<0:
        return("Factorial does not exist for negative no")
    elif num==0:
        return 1
    else:
        fact=1
        for i in range(1,num+1):
            fact =fact*i
            return fact
n=int(input("Enter a positive integer(n):"))
factorial=factorial(n)
if n<1:
   print("Please enter a positive integer greater the or equal to 1")
else:
   print(f"Factorial from 1 to {n}")
   for j in range(1,n+1):
       result=factorial(j)
       print("factorial of {j} is {result}")
