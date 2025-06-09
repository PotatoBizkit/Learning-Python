# Program to sum a list of 4 no.
lis_of_no=[]
sum = 0
print("Enter the 4 numbers you want the sum of:")
for i in range(4):
    lis_of_no.append(int(input()))
for i in range(4):
    sum+=lis_of_no[i]
print("The sum of numbers is", sum)