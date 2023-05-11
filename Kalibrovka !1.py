from random import randint
n = (open("words.txt", "r"))
f = n.read()
d = f.split(",")

c = d[randint(0, len(d) - 1)]
print(c)
s = list(c)
print(s)
for i in range(0, len(c), 2):
    rand = randint(0, len(c)-1)
    s[rand] = "_"
    print(i)
print("".join(s))

while True:
    if ______ == c:
        mesege.ansver("Gg")
        break
