manga_authors = {"Kentaro Muira": "Berserk", "Tatsuki Fujimoto": ["Chainsaw Man", "Fire Punch"], "Tatsuya Endo": "SpyxFamily"}
print(manga_authors["Kentaro Muira"])
print(manga_authors["Tatsuki Fujimoto"][1])
for i in manga_authors.items():
    print(i)
for i in manga_authors.keys():
    print(i)
manga_authors.pop("Tatsuki Fujimoto")
for i in manga_authors.keys():
    print(i)
manga_authors.update({"Naoki Urasawa":["Pluto", "Monster"]})
for i in manga_authors.items():
    print(i)