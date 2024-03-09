adad_str = input()
adad_int = int(adad_str)
def sum_digits(adad_int):
    if adad_int >= 10:
        for ragham in adad_str:
            adad_int = adad_int + int(ragham)
    adad_int = adad_int - int(adad_str)    
    return adad_int
while adad_int >= 10:
    adad_str = str(adad_int)
    adad_int = sum_digits(adad_int)
else:
    print(adad_int)