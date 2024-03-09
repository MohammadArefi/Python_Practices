def b_m_m(a,b):
    if b == 0:
        return a
    elif a > b:
        return b_m_m(b,a % b)
    else:
        return b_m_m(a,b % a)


A = int(input())
B = int(input())
print(b_m_m(A,B))