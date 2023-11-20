from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

# res:List[str] = list(map(lambda x,y:x,y,numbers,str(letters)))

# print(res)

def f():return map(None, letters, numbers)


f()

