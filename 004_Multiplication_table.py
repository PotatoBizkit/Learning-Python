num = int(input("Input the number you want multiplication table of: "))
print(f"The multiplication table of {num} is:")
for i in range(1,11):
    print(f"{num} x {i} = " + str(num*i))