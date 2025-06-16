# Program to take numbers as inputs and display unique numbers.

s = set()
# print(type(s))
x = int(input("How many numbers you want to enter?\n"))
print("Enter",x,"numbers:")
for i in range(x):
    s.add(int(input("")))
print("The unique numbers are:\n",s)