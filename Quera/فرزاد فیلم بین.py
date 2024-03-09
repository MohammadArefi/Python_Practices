a = int(input())
b = []
for i in range(a):
    c = input()
    d = c.lower()
    b.append(d)

f = []
for j in b:
    e = j.title()
    f.append(e)

g = '\n'.join(map(str,f))
print(g)