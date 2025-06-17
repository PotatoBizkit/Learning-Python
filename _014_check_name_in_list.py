# Program to check if given name exists in list
import difflib

name = ['chainsaw man', 'hells paradise', 'one piece', 'vagabond', 'berserk', 'hellsing']

cname = input("Enter manga name you want to search:\n")

close_matches = difflib.get_close_matches(cname.strip().lower(), [m.lower() for m in name], n=1, cutoff=0.6)


if (cname.strip().lower() in [m.strip().lower() for m in name]):
    print("It exists")
elif close_matches:
    print(f"It does not exist. Did you mean: {close_matches[0]}?")
else:
    print("Similar to your love life, it does not exist")