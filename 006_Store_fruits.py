# Program to store fruits entered by user
lof = []
x = input("Do you want to list fruits?\nEnter 'Y' for yes and 'N' for no\n")
if (x.lower()=='y'):
    print("Enter 'Q' to quit listing\n")
    frts=''
    print("Enter the list of fruits:")
    while(frts.lower()!='q'):
        frts=input("")
        if(frts.lower()!='q'):
            lof.append(frts)
    print("This is your list\n"+str(lof))
elif (x.lower()=='n'):
    print("Alrighty!")
else:
    print("Enter valid option!")