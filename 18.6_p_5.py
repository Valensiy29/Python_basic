import re
import requests


response = requests.get('http://www.columbia.edu/~fdc/sample.html').text

result_beta = re.findall(r'>.+</h3>', response)
print(result_beta)