num = int(input("Enter the num you want factorial of:\n"))

if (num==0 or num == 1):
   print(f"Factorial of {num} is 1")
elif (num>0):
    x=1
    for i in range(1, num+1):
        x*=i
    print(f"Factorial of {num} is {x}")
else:
    print("not valid input")