from collections import Counter


def poly(val: str) -> bool:
    return 2 >=len(list(filter(lambda x: x% 2,Counter(val).values())))

print(poly('ababc'))
print(poly('abbbbbc'))

