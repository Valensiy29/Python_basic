data = {1:2,3:4}
result = ''
if type(data) == str or type(data) == float or type(data) == bool or type(data) == tuple or type(data) == int:
    result = 'immutable'
else:
    result = 'mutable'

print(type(data),id(data),result)