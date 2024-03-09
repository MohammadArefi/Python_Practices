tedad_horoof = int(input())
kalame_dorost = input()
kalame_voroudi = input()
liste_voroudi = list(kalame_voroudi)
liste_dorost = list(kalame_dorost)
zip_object = list(zip(liste_dorost,liste_voroudi))
tafavote = []
for i in zip_object:
    if i[0] != i[1]:
        tafavote.append(i[1])
    
print(len(tafavote))