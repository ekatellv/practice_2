money = float(input('Введите значение общей стоимости часов:'))
number_silver= 96
number_gold = number_silver / 16
price_silver = number_silver * 48
print(round((money - price_silver)/number_gold))
