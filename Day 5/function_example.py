coffee_prices = [('cappuccino', 1.5),
                 ('espresso', 2.2),
                 ('mocha', 1.9)]

for element in coffee_prices:
    print(element)

for coffee, price in coffee_prices:
    print(coffee)

def most_expensive_coffee(list_of_prices):

    highest_price = 0
    my_most_expensive_coffee = ''

    for kawa, cena in list_of_prices:
        if cena > highest_price:
            highest_price = cena
            my_most_expensive_coffee = kawa
        else:
            pass
    return  (my_most_expensive_coffee, highest_price)
print(most_expensive_coffee(coffee_prices))
coffee, price = most_expensive_coffee(coffee_prices)
print(f'The most expensive coffee is {coffee}, whose price is {price}')
