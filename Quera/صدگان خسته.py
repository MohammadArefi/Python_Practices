adade_aval = int(input())
adade_dovom = int(input())
def barakse_adad(n):
    sum = 0
    while n > 0:
        a = n % 10
        sum = sum * 10 + a
        n = n // 10
    return sum

barakse_adade_aval = barakse_adad(adade_aval)
barakse_adade_dovom = barakse_adad(adade_dovom)

if barakse_adade_aval > barakse_adade_dovom:
    print(adade_dovom,end = ' < ')
    print(adade_aval)

elif barakse_adade_dovom > barakse_adade_aval:
    print(adade_aval,end = ' < ')
    print(adade_dovom)
else:
    print(adade_dovom,end = ' = ')
    print(adade_aval)
    
