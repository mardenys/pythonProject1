def check_3_digits(list):

    three_digits_list = []

    for n in list:
        if n in range(100, 1000):
            three_digits_list.append(n)
        else:
            pass

    return three_digits_list

result = check_3_digits([532, 99, 380])
# print(type(result))
# print(result)

def all_positives(list):
    for n in list:
        if n < 0:
            return False
        else:
            pass
    return True

numbers = [11,4,-5]
result = all_positives(numbers)
# print(result)

numbers = [1,212,424,212]
def sum_less(numbers):
    result = 0
    for n in numbers:
        if n in range(1,1000):
            result += n
        else:
            pass
    return result
sum = sum_less(numbers)
print(sum)

numbers = [1,212,422,2122]
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count +=1
        else:
            pass
    return count

result = count_even(numbers)
print(result)



