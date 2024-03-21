# Comment créer une classe

class Item:
    def calculate_total_price(self, x, y):
        return x +y


# Comment créer une instance de classe
item1 = Item()

# Attribuer des attributs
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# Appel de méthodes à partir d'instances d'une classe :
print(item1.calculate_total_price(item1.price, item1.quantity))

# Comment créer une instance d'une classe (nous pouvons créer autant d'instances que nous le souhaitons)
item2 = Item()

# Attribuer des attributs
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# Appel de méthodes à partir d'instances d'une classe :
print(item2.calculate_total_price(item2.price, item2.quantity))