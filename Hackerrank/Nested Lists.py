if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])

    def Sort(sub_li):
    
        sub_li.sort(key = lambda x: x[1])
        return sub_li
    sort_lst = Sort(lst)
    
    # remove duplicates
    nmin = min(sort_lst, key = lambda y : y[1])
    new_lst = []
    for item in sort_lst:
        if item[1] != nmin[1]:
            new_lst.append(item)
            
    final_lst = []            
    nmin1 = min(new_lst, key = lambda z : z[1])
    for jtem in new_lst:
        if jtem[1] == nmin1[1]:
            final_lst.append([jtem][0][0])

    final_lst = sorted(final_lst)
    print(*final_lst, sep = '\n')
