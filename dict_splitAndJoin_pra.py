my_dict = {'A': 2, 'B': 3, 'C': 4}

#How to find the key of a value
keys = list(my_dict.keys())
values = list(my_dict.values())

findKey = values.index(3)
print(keys[findKey])  #prints B


a = '-'
answer = a.join(['A', 'B', 'C'])
print(answer) #prints A-B-C

