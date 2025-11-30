def month(n):
    months = ["January", "February", "March", "April", 
        "May", "June", "July", "August", 
        "September", "October", "November", "December"]

    if 1 <= n <=12:
        return months[n-1]
    else:
        return "Invalid month number"

   
# Ten fragment wykona się tylko przy bezpośrednim uruchomieniu tego pliku
if __name__ == "__main__":
    print("Test modułu:")
    print(month(8))   # Powinno wypisać January
    print(month(12))  # Powinno wypisać December