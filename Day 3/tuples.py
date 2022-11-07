my_tuple = (1, 2, (10, 20), 4)
#my_tuple = list(my_tuple)
print(type(my_tuple))

t = (1, 2, 3)
x,y,z = t
print(x, y, z)

t = (1, 2, 3, 1)
print(t.count(2))
print(t.index(1))