from typing import Counter

range_khoraki = input()
list_range_khoraki = []
for i in range_khoraki:
    list_range_khoraki.append(i)

red_count = list_range_khoraki.count('R')
yellow_count = list_range_khoraki.count('Y')
green_count = list_range_khoraki.count('G')

if red_count == 3 or red_count == 4 or red_count == 5:
    print('nakhor lite')
elif (red_count == 2 and yellow_count == 2) or (red_count == 2 and yellow_count == 3) or (red_count == 3 and yellow_count == 2):
    print('nakhor lite')
elif green_count == 0:
    print('nakhor lite')
else:
    print('rahat baash')