my_set = set([1, 2, 3, 4, 5])
print(type(my_set))
print(my_set)

# other_set = {1 ,2, 3}
# print(type(other_set))
# print(other_set)

s1 = {1, 2, 3}
s1.clear()
print(s1)
#s1.add(6)
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

my_set_1 = {1, 2, "three", "four"}
my_set_2 = {"three", 4, 5}
my_set_3 = my_set_1.union(my_set_3)
