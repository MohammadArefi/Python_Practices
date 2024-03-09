voroudi = input().split()
radif_sandali = list(map(int,voroudi))
if radif_sandali[1] <= 10:
    print('Right' , end = ' ')
    print(10 - radif_sandali[0] + 1 , end = ' ')
    print(radif_sandali[1])
elif radif_sandali[1] > 10:
    print('Left' , end = ' ')
    print(10 - radif_sandali[0] + 1 , end = ' ')
    print(20 - radif_sandali[1] + 1)
