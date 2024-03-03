if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = set(list(arr))
    lst1 = sorted(list(lst))
    print(lst1[-2])
    