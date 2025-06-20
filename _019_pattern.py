# Program to print pattern:
#     *
#    ***
#   *****

def triangle(rows):
    for i in range(1, rows+1):
        print(" "*(rows-i), end='')
        for j in range(1, 2*i):
            print("*", end='')
        print()

row = int(input("Enter the number of rows you want:\n"))
triangle(row)