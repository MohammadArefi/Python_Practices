a = input()
b = a.split()
c = list(map(int,b))

if c[0] == c[2]:
    print('Vertical')
elif c[1] == c[3]:
    print('Horizontal')
else:
    print('Try again')
