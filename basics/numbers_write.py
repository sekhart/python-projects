import json

numbers = [2, 3, 5, 7, 11, 13, 'One']
filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj);

with open(filename, 'r') as fr_obj:
    nos = json.load(fr_obj)
    print(nos)
