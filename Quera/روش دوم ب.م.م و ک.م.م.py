def b_m_m(a,b):
    r = 1
    while (r != 0):
        r = a % b
        a = b 
        b = r
    return a 


def k_m_m(a,b,z):
    p = a * b
    return p // z


n, m = [int(n) for n in input().split()]
z = b_m_m(n,m)
q = k_m_m(n,m,z)
print(z,q)