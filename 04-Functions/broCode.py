# def display_invoice(username, amount, due_date):
#     print(f"hello {username}")
#     print(f"Your bill of ${amount:.2f} is due {due_date}")



# display_invoice("Michał", 435.50, "09/01")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()


    return first + " " + last 


full_name = (create_name("michał", "motor"))

print(full_name)