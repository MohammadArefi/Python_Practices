voroudi = input().split()
tedad_arar_va_zaman_bein_arar = list(map(int,voroudi))
sum = 0
for i in range(1,tedad_arar_va_zaman_bein_arar[2] + 1):
    if i % 2 == 1:
        sum = sum + tedad_arar_va_zaman_bein_arar[0]
    elif i % 2 == 0:
        sum = sum + tedad_arar_va_zaman_bein_arar[1]

print(sum)

