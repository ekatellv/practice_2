weight = float(input('Введите свой вес в фунтах:'))
length = float(input('Введте свой вес в дюймах:'))
print(round((weight*0.453592)/((length*2.54)/100)**2, 2))
