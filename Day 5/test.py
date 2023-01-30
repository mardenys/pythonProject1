numbers = [1, 2, 15, 7, 2]
def reduce_list(numbers):
    unique = list(set(numbers))
    unique.remove(max(unique))
    return unique




def average(numbers):
    return sum(numbers)/len(numbers)

reduced = reduce_list(numbers)
result = average(reduced)
