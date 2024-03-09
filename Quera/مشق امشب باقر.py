a = input().split()
b = map(int,a)
c = list(b)
if 0 in c :
    print('No')
elif sum(c) == 180:
    print('Yes')
else :
    print('No')

