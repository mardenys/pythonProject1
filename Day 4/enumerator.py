my_list = ['a', 'b', 'c']
for index, item in enumerate(my_list):
    print(index, item)

my_list = ['a', 'b', 'c']
my_tuples = list(enumerate(my_list))
print(my_tuples[1][1])

list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
for index, name in enumerate(list_names):
    print(f"{name} is found at index {index}")

indices_list = list(enumerate("Python"))
print(indices_list)

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
for index, name in enumerate(list_names):
    if name[0] == "M":
        print(index)