class VendingMachine:
    def __init__(self, location):
        self.location = location
        self.balance = 0
        self.inventory = {}

    def add_product(self, name, price):
        # dodaje nowy produkt do slownika lub aktualizuje cene istniejacego
        name = name
        price = price
        if not self.inventory.get(name):
            print(f"produkt nie istnieje wiec, juz go dodajemy")
        else:
            self.inventory[name] = price
            print(f"produkt {name} juz istnieje, ale zmienilismy jego cene!")
            
        self.inventory[name] = price

    def insert_money(self, amount):
        amount = amount
        self.balance += amount

    def buy_product(self, name):
        self.name = name
        if self.inventory.get(name):
            if self.inventory.get(name) <= self.balance:
                self.balance -= self.inventory.get(name)
                print(f"Kupiono: {name}")
            else:
                print("Brak środków!")
        else:
            print(f"Nie ma takiego produktu!")

    def __str__(self):
        napis = (f"Lokalizacja automatu: {self.location}, ")
        napis +=(f"aktualne saldo: {self.balance}, ")
        napis += "Dostępne produkty: \n"
        
        for produkt, cena in self.inventory.items():
            napis += (f"{produkt}: {cena} PLN ")
            
        return napis

automat = VendingMachine("Biblioteka")
automat.add_product("Cola", 5.50)
automat.add_product("Baton", 3)
automat.add_product("Woda", 2.50)
print(automat)
automat.insert_money(5)
automat.buy_product("Cola")
automat.insert_money(2)
automat.buy_product("Cola")
print(automat)
