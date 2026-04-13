def calculate():
        num1=float(input("Enter first no:"))
        num2=float(input("Enter second no:"))
        op=input("Enter the operator:")
        if op == '+':
            return num1+num2
        elif op =='-':
            return num1-num2
        elif op=='*':
            return num1*num2
        elif op=='/':
            return num1/num2
        else:
            result =("Invalid operator")
        print("Result:",result)

calculate()
