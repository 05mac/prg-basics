# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99, 'chleb': 2.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2,'pep': 2}

koszt = 0
for key, value in cart.items():
    if key in prices:
        koszt += value * prices[key]


print(koszt)