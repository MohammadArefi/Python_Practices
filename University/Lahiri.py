b = []
M = int(input('Enter the max of xi : '))
N = int(input('Enter the number of society : '))
n = int(input('Enter the number of sample : '))

count = 0
while (n != count):
    i = int(input('Enter number between 1 , {0} : '.format(N)))
    if i not in range(1,N):
        raise ValueError('Enter correct i between 1 , {0}'.format(N))
    j = int(input('Enter number between 1 , {0} : '.format(M)))
    if j not in range(1,M):
        raise ValueError('Enter correct j between 1 , {0}'.format(M))
    xi = int(input('Enter xi : '))
    if xi > j :
        b.append(i)
        count += 1

print(b)

