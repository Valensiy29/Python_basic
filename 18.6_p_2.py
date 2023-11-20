import re

numers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'


result = re.findall(r'\b[А-У]\d{3}\w[А-У]\d{3}\b',numers)
print(result)

taxi = re.findall(r'\b\w[А-У]\d{0,6}\b',numers)
print(taxi)