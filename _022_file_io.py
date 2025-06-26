import re

# add = "My dress-up darling is best romcom manga."

# f = open("lol.txt", "a")
# f.write(add)
# f.close()

# print(open("lol.txt").read())
# open("lol.txt").close()

with open("lol.txt", "a+") as f:
    # f.write("\nJJK is cool.")
    f.seek(0)
    # print(f.read())
    text = f.read()
    word = "jjk"
    pattern = rf'\b{re.escape(word.lower())}\b'
    if re.search(pattern, text.lower()):
        print(word, "exists")
    else:
        print(word, "does not exist")