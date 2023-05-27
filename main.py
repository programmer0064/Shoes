from Shoes import Shoes

air_force = Shoes("Air force", 120)
yeezy = Shoes("Yeezy", 400)

try:
    shoes_budget = float(input("What is your budget"))
except ValueError():
    print("Give a number")

for shoe in [air_force, yeezy]:
    shoe.buy(shoes_budget)