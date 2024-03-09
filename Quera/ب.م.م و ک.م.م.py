def b_m_m(a,b):
    if b == 0:
        return a
    elif a > b:
        return b_m_m(b,a % b)
    else:
        return b_m_m(a,b % a)


def k_m_m(a,b,z):
    p = a * b
    return p // z

n, m = [int(n) for n in input().split()]
z = b_m_m(n,m)
q = k_m_m(n,m,z)
print(z,q)
