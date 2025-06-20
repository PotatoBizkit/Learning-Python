# Program to print pattern:
#     *
#    ***
#   *****

def triangle(rows):
    """
    Prints a equilateral triangle pattern using asterisks.

    Parameters:
    rows (int): The number of rows in the triangle.

    Returns:
    None
    """
    for i in range(1, rows+1):
        print(" "*(rows-i), end='') # comment out this line to print lower triangular pattern
        for j in range(1, 2*i):
            print("*", end='')
        print()

row = int(input("Enter the number of rows you want:\n"))
triangle(row)