a = input()
b = a.split()
n = int(b[0]) 
s = b[1]
copy = 'copy of '
for i in range(n):
    print(copy,end = '')
print(s)