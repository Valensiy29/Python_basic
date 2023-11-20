import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

result = re.findall(r'\b[aeuioAEUIO]\w+',text)

result_2 = re.findall(r'\b[qwrtypsdfghjklzxcvbnm]\w*',text.lower())