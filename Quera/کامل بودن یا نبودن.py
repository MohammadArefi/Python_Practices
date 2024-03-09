N = int(input())
sum = 0
for i in range (1,(N//2)+1):
    b = N / i
    c = N % i
    if (c==0):
        sum=sum+i
if sum == N:
    print('YES')
else:
    print('NO')
