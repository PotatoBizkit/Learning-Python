# Program to print pattern of kind:
# * * *
# *   *
# * * *

def box_pattern(rows):
    for i in range (1, rows+1):
        if i == 1 or i == rows:
            print("@ "*rows)
        else:
            print("@"+" "*(2*(rows-2)+1)+"@")

row = int(input("Enter the number of rows you want:\n"))
box_pattern(row)