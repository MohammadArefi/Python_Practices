a = int(input())
b = input()
c = int(input())
d = input()
e = int(input())
f = input()
b_1 = b.split()
d_1 = d.split()
f_1 = f.split()
last_list_1 = b_1 + d_1 + f_1
last_list_2 = list(set(last_list_1))
list_asli = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome']
list_nahaei = []
for i in last_list_2:
    if i in list_asli:
        list_nahaei.append(i)

print(7 - len(list_nahaei))
