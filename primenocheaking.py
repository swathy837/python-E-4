import math
def is_prime(n):
    if n<2:
        return false
    for i in range (2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def check_sum_of_prime(n):
    check_sum_of_prime=int(input("Enter the prime no:"))

    found=False
    for i in range(2,n//2+1):
        if is_prime(n):
            print(f"{n}={i}+{n-i}")
            found=True
            break
        if not found:
            print("{n} cannot be exposed as sum of two primes.")
num=int(input("Enter the no:"))
check_sum_of_prime(num)
