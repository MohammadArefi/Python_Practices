a = int(input())
b = []
b.append(a)
while a != 0:
    a = int(input())
    b.append(a)

c = list(reversed(b))
for i in c:
    if i != 0 :
        print(i)
