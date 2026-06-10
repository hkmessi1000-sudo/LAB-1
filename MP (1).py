def greet():
    print("🍽 Welcome to Food Corner 🍽")

def menu():
    items = {
        1: "Burger",
        2: "Pizza",
        3: "Sandwich",
        4: "French Fries",
        5: "Soft Drink"
    }

    print("\nMenu")
    for i in items:
        print(i, ".", items[i])

    ch = int(input("Enter your choice (1-5): "))

    if ch == 1:
        burger()
    elif ch == 2:
        pizza()
    elif ch == 3:
        sandwich()
    elif ch == 4:
        fries()
    elif ch == 5:
        drink()
    else:
        print("Invalid Choice")

def bill(items, ch, q):
    item = items[ch]["name"]
    price = items[ch]["price"]

    total = price * q

    print("\n🍽 Food Corner Bill 🍽")
    print("---------------------")
    print("Item     :", item)
    print("Quantity :", q)
    print("Price    : Rs.", price)
    print("---------------------")
    print("Total    : Rs.", total)
    print("---------------------")
    print("Thank You! Visit Again 😊")

def burger():
    items = {
        1: {"name": "Veg Burger", "price": 50},
        2: {"name": "Cheese Burger", "price": 90},
        3: {"name": "Chicken Burger", "price": 120}
    }

    print("\nBurger Menu")
    for i in items:
        print(i, ".", items[i]["name"], "- Rs.", items[i]["price"])

    ch = int(input("Enter the choice: "))
    q = int(input("Enter the quantity: "))
    bill(items, ch, q)

def pizza():
    items = {
        1: {"name": "Margherita", "price": 150},
        2: {"name": "Farmhouse", "price": 190},
        3: {"name": "Chicken Pizza", "price": 250}
    }

    print("\nPizza Menu")
    for i in items:
        print(i, ".", items[i]["name"], "- Rs.", items[i]["price"])

    ch = int(input("Enter the choice: "))
    q = int(input("Enter the quantity: "))
    bill(items, ch, q)

def sandwich():
    items = {
        1: {"name": "Veg Sandwich", "price": 50},
        2: {"name": "Cheese Sandwich", "price": 90},
        3: {"name": "Grilled Sandwich", "price": 130}
    }

    print("\nSandwich Menu")
    for i in items:
        print(i, ".", items[i]["name"], "- Rs.", items[i]["price"])

    ch = int(input("Enter the choice: "))
    q = int(input("Enter the quantity: "))
    bill(items, ch, q)

def fries():
    items = {
        1: {"name": "Small Fries", "price": 50},
        2: {"name": "Medium Fries", "price": 85},
        3: {"name": "Large Fries", "price": 110}
    }

    print("\nFrench Fries Menu")
    for i in items:
        print(i, ".", items[i]["name"], "- Rs.", items[i]["price"])

    ch = int(input("Enter the choice: "))
    q = int(input("Enter the quantity: "))
    bill(items, ch, q)

def drink():
    items = {
        1: {"name": "Coke", "price": 40},
        2: {"name": "Pepsi", "price": 40},
        3: {"name": "Thumbs up", "price": 40}
    }

    print("\nDrinks Menu")
    for i in items:
        print(i, ".", items[i]["name"], "- Rs.", items[i]["price"])

    ch = int(input("Enter the choice: "))
    q = int(input("Enter the quantity: "))
    bill(items, ch, q)

greet()

while True:
    menu()

    x = input("\nDo you want to continue? (yes/no): ")
    if x.lower() == "no":
        print("Thank You Visit again!")
        break
