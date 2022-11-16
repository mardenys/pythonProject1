my_list = [letter for letter in 'pythksd fdo[f fsd[pkfds']
print(my_list)

my_list = [n if n * 2 > 10 else 'no' for n in range(0 ,21, 2)]
print(my_list)

feet = [10, 20, 30, 40, 50]
meters = [f * 0.3048 for f in feet]
print(meters)

values = [1, 2, 3, 4, 5, 6, 9.5]
square_values = [sq**2 for sq in values]
print(square_values)

even_values = [even for even in values if even%2==0]
print(even_values)

temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(degrees_fahrenheit-32)*(5/9) for degrees_fahrenheit in temperature_fahrenheit]

ran = list(range(0,6))
print(ran)