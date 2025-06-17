num_lst = []
print("Enter 4 numbers:")
for i in range(4):
    num_lst.append(int(input("")))

if (num_lst[0] == num_lst[1] == num_lst[2] == num_lst[3]):
    print("The numbers are equal")
else:
    print("The greatest number is", maxnum)