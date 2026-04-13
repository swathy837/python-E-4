def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Enter the no:"))
print({"The {n} the fibonacci no is {fibonacci (n)}")
