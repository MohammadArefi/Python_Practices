tedad_mohrehaye_voroudi = input() 
list_str_tedad_mohrehaye_voroudi = tedad_mohrehaye_voroudi.split()
list_int_tedad_mohrehaye_voroudi = list(map(int,list_str_tedad_mohrehaye_voroudi))
tedad_mohrehaye_sahih = [1, 1, 2, 2, 2, 8]
tafavote_tedad_mohreha = []
zip_object = zip(tedad_mohrehaye_sahih , list_int_tedad_mohrehaye_voroudi)
for tedad_mohrehaye_sahih_i , list_int_tedad_mohrehaye_voroudi_i in zip_object:
    tafavote_tedad_mohreha.append(tedad_mohrehaye_sahih_i - list_int_tedad_mohrehaye_voroudi_i)

for i in tafavote_tedad_mohreha:
    print(i , end = ' ')

