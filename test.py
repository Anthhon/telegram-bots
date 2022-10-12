# from random import choice


# cList = [
#     'escolha 1',
#     'escolha 2',
#     'escolha 3'
# ]

# x = choice(cList)

# print(x)

# from datetime import date
# d0 = date.today()
# d1 = date(2022, 10, 30)
# delta = d1 - d0
# print('The number of days between the given range of dates is :')
# print(delta.days)

# from forex_python.converter import CurrencyRates

# # print(c.get_rates('USD')) # you can directly call get_rates('USD')
# c = CurrencyRates()
# currency = c.get_rates('USD')

# print(currency)
# print(f"O dólar está valendo {round(currency['BRL'], 2)} reais!")

from datetime import datetime
ts = int('1665595015')

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%M'))
print(type(datetime.utcfromtimestamp(ts).strftime('%M')))