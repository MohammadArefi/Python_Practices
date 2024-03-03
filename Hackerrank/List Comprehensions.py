if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())        
    lst = [[item, jtem, ktem] 
                                for item in range(0, x + 1)
                                    for jtem in range(0, y + 1)
                                        for ktem in range(0,z + 1) 
                                            if item + jtem + ktem != n]
    
    print(lst)