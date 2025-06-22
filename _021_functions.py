def greatest_of_3_no():
    try:
        a = int(input("Enter first integer:\n"))
        b = int(input("Enter second integer:\n"))
        c = int(input("Enter third integer:\n"))
        print("The greatest number is", max(a, b, c))
    except Exception as e:
        print(e)


def celcius_to_farhenheit():
    try:
        a = float(input("Enter temperature in celcius:\n"))
        print("The temperature in fahrenheit is", (((9/5)*a)+32))
    except Exception as e:
        print(e)


def sum_n_natural_numbers(num):
    if num < 0:
        raise ValueError("n must be non-negative")
    return num * (num + 1) // 2
    # / -> is actual division that returns float value
    # // -> is floor division that returns int value


def main():
    while (1):
        print("""
Welcome! What would you like to do?
0. Exit
1. Find greatest of 3 numbers
2. Convert celcius to farhenheit
3. Calculate first n natural numbers
""")
        
        try:
            x = int(input("Enter your choice: "))
        except ValueError:
            print("👉 Please enter a valid number.")
            continue

        match x:
            case 0:
                print("Thank You ^_^")
                break
            case 1:
                greatest_of_3_no()
            case 2:
                celcius_to_farhenheit()
            case 3:
                try:
                    n = int(input("Enter the number of natural numbers you want sum of:\n"))
                    s = sum_n_natural_numbers(n)
                    print("The sum of first", n, "natural numbers is:", s,)
                except Exception as e:
                    print(e)
            case _:
                print("Try again!")

if __name__ == "__main__":
    main()