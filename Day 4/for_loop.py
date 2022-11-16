my_list = ['a', 'b', 'c']

for letter in my_list:
    letter_number = my_list.index(letter) + 1
    print(f"letter {letter_number}: {letter}")

for slowa in "python":
    print(slowa)

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_even = 0
sum_odd = 0
for number in list_numbers:
    if number % 2 == 0:
        sum_even = sum_even + number
    else:
        sum_odd = sum_odd + number
print(sum_even)
print(sum_odd)