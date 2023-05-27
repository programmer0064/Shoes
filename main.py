from Shoes import Shoes

air_force = Shoes("Air force", 120) #mit Shoes() kreieren wir eine neue Klasse und speichern dieses Objekt in der Variable air_force. Beim Erstellen eines Objekts wird Speicherplatz reserviert. Die Adresse des Speicherplatzes wird in der Variable air_force gespeichert.
yeezy = Shoes("Yeezy", 400)

try:
    shoes_budget = float(input("What is your budget"))
except ValueError():
    print("Give a number")

for shoe in [air_force, yeezy]:
    shoe.buy(shoes_budget)