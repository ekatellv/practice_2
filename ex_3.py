chocolate = (input('Введите стоимость шоколадок через пробел:')).split()
print(int(chocolate[0])+int(chocolate[1]))

#using map
S, R = map(int, input('Введите цены шоколадок через пробел:').split())
print(S+R)
