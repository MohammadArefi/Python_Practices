nomre = int(input())
tedad_roozhaye_safar = int(input())
if tedad_roozhaye_safar == 0:
    print(20)
elif tedad_roozhaye_safar == 7:
    print(nomre)
else:
    if nomre - tedad_roozhaye_safar <= 0:
        print(0)
    else:
        print(nomre - tedad_roozhaye_safar)
