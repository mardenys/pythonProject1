my_dictionary = {'c1':'value1', 'c2':'value2'}
print(type(my_dictionary))

result = my_dictionary['c1']
print(result)


customer = {'name':'John','last_name':'Lennon','weight': 88, 'height': 1.76}

query = customer['height']
print(query)

dic = {1: 55, 2: [10, 20, 30], 3: {'s1':100, 's2': 200}}
print(dic[3]['s1'])

dict = {'k1': ['a', 'b', 'c'], 'k2':['d', 'e', 'f']}
dict['k3'] = ['g']
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict['k2'][1].upper())

my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
my_text = (my_dict['points'])
print(my_text['points2'][1])

my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict["points"]["points2"][1])


my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict['age'] = 36
my_dict['occupation'] = 'Editor'
my_dict['country'] = 'Colombia'
print(my_dict)