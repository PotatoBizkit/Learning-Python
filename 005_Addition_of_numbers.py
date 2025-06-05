try:
    noita = int(input("Enter the number of integers you want to add:\n"))
    num = 0
    for i in range(noita):
        num += int(input(f"Enter integer number {i+1}:\n"))
    print(f"The sum of all integers is {num}")
except ValueError:
    print("Just enter intrgers")