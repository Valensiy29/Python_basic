import re

phone_num = str(['9999999999', '999999-999', '99999x9999'])

result_2 = re.findall(r'\b[8,9]\d{9}\b', phone_num)