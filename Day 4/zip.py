names = ['Hanna', 'Bruce', 'Tony']
ages = [65, 29, 42]
cities = ['New York', 'London', 'Madrid']
combination = list(zip(names, ages, cities))

for name, age, city in combination:
    print(f'{name} is {age}, and lives in {city}')

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]
zipped = list(zip(capitals, countries))

for capital, country in zipped:
    print(f'The capital of {country} is {capital}')