def find_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_prime(m):
    if m < 2:
        return False
    for j in range(2,m // 2 + 1):
        if m % j == 0:
            return False 
    return True


prime_divisors = []
def find_divisors_is_prime(x):
    a = find_divisors(x)
    for k in a :
        if is_prime(k) == True:
            prime_divisors.append(k)
    return prime_divisors

c = []
for h in range(10):
    d = int(input())
    c.append(d)

b = {}
for l in c :
    e = find_divisors_is_prime(l)
    f = len(e)
    b[l] = f

print(b)



