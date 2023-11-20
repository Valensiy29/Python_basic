#f_year = int(input('повышение  на первый год'))
# sec_year = int(input('повышение на второй год'))
# sum = 0
# new = []
# for i in range(0,5):
#     prod = [float(input('цена на товар'))]
#     sum = [i for i in prod]
# for num in range(2):
#     for i in prod:
#         new.append(i / 100 * f_year)
# print(new)

prices = [float(input("Цена на товар: ")) for _ in range(5)]

first_year = int(input("Повышение на первый год: "))
second_year = int(input("Повышение на второй год: "))

all_prices = 0
for percent in 0, first_year, second_year:
    prices = [price * (1 + percent / 100) for price in prices]
    all_prices += round(sum(prices), 2)

print(all_prices)