name = input("What is your name: ")
sales = int(input("How much did you sold? "))
commision = round(sales * 0.13 / 100,2)

print(f"You {name} sold {sales} and earn commission equal to {commision}")

