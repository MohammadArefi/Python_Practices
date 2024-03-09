def prime(m):
    if m < 2:
        return False
    for i in range(2,m//2+1):
        if m % i == 0:
            return False
    return True

def total_figures(x):
    l = []
    while x != 0:
        yekan = x % 10
        l.append(yekan)
        x = x // 10
    sum = 0
    for i in l:
        sum = i + sum
    return sum

def find_sum_omin_prime(y):
    l1 = []
    z = total_figures(y)
    y = y + 1
    while len(l1) != z:
        if prime(y) == True:
            l1.append(y)   
        y = y + 1
    return l1[-1]

n = int(input())
print(find_sum_omin_prime(n))
