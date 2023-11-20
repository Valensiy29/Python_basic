import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match('wo',text)

result_2 = re.search('wo',text)

result_2.start()

result_2.end()

result_3 = re.findall('wo',text)

result_4 = re.sub('wo','замена',text)