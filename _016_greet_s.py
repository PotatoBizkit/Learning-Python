# Program to greet names starting with s from list l1

l1 = ['Tony', 'Steve', 'Stark', 'Rogers']

# for i in l1:
#     if i.startswith('S'):
#         print("Hello " + i + "!")

print("\n".join(f"Hello {name}!" for name in l1 if name.startswith("S")))

i=0
while i < len(l1):
    if l1[i].startswith('S'):
        print(f"Hi {l1[i]}!")
    i+=1