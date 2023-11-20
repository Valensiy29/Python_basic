import random

frs_tour = [random.uniform(5,10) for _ in range(20)]
sec_tour = [random.uniform(5,10) for _ in range(20)]
final = [(frs_tour[num] if frs_tour[num] > sec_tour[num] else sec_tour[num])for num in range(20)]

print('Победители тура',final, len(final))