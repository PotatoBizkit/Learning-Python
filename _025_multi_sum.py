# Given two integer numbers, write a Python program to return their product 
# only if the product is equal to or lower than 1000. Otherwise, return their sum.

n1 = int(input("Enter first number:\n"))
n2 = int(input("Enter second number:\n"))

if n1*n2<=1000:
    print(n1*n2)
else:
    print(n1+n2)
