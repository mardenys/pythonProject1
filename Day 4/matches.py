series = "N-02"

match series:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("This product doesnt exist")

client = {'name': 'Federico',
          'age': 46,
          'occupation': 'instructor'}

movie = {'title': 'Matrix',
         'credits':{'main_star': 'Keanu Reaves',
                    'director': 'J Wachoesky'}}

items = [client, movie, 'book', movie]

for i in items:
    match i:
        case {'name': name,
              'age': age,
              'occupation': occupation}:
            print("It is a client")
            print(name, age, occupation)
        case {'title': title,
              'credits': {'main_star': main_star,
                          'director': director}}:
            print("This is a movie")
            print(title, main_star, director)

        case _:
            print("I dont know what it is")
