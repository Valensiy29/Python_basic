import random
f_num = int(input('выберите диапазон от'))
sc_num = int(input('до'))
original_prices = [random.randint(f_num,sc_num) for _ in range(5)]

new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices),max(original_prices),min(new_prices),new_prices.reverse())