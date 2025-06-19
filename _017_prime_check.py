# Program to check if given no. is prime
import math

num = int(input('Enter a no.:\n'))

prime = 1
for i in range(2, int(math.sqrt(num)+1)):
    if num%i==0:
        prime = 0
        break

if prime == 1:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")