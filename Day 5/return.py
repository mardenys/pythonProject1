def multiply(number1, number2):
    return number1 * number2

result = multiply(5,4)
print(result)

def power(first,second):
    return first**second

result = power(3,4)
print(result)

def usd_to_eur(usd):
    return usd*0.9

dollars = 55
conv = usd_to_eur(dollars)

print(conv)

word = "puThon"
def reverse_word(word):
    word = word[::-1]
    word = word.upper()
    return word

result = reverse_word(word)

print(result)