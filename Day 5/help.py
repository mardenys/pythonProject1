dic = {'key1': 100, 'key2': 500}

x = dic.popitem()
print(x)
print(dic)


text = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
a = text.lstrip(',:%_#')
print(a)

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
b = fruits.insert(3, 'orange')
print(fruits)

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}
c = phone_brands.isdisjoint(tv_brands)
print(c)