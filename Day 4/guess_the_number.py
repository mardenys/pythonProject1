from random import randint
print("Hey, what is your name?")
name = input()
print(f"Hi {name}, guess a number between 1 and 100 in 8 tries maximum.")

guess_number = 0
random_number = randint(1,100)
#print(random_number)
print("What number do you think it is?")
while guess_number < 8:
    guess = int(input("Input number: "))
    guess_number = guess_number + 1

    if guess < random_number and guess > 0:
        print("too low")
    if guess > random_number and guess <= 100:
        print("too high")
    if guess <= 0:
        print("number must be higher than 0")
    if guess > 100:
        print("Number must be lower than 101")
    if guess == random_number:
        break

if guess == random_number:
    print(f'Well done {name}, {guess} is the correct number. Number of tries to guess it: {guess_number}')

if guess != random_number:
    print(f"Sorry {name}, you run out of tries. Correct number was {random_number}")
