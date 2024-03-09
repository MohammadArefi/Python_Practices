def prime(n):
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
c = []
for i in range(a+1,b):
    if prime(i) == True:
        c.append(i)

print(",".join(str(i) for i in c))