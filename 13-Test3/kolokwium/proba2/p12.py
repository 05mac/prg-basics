import re
def f(dates):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    wynikowa_lista = []
    dates = dates.split(",")
    
    for date in dates:
        if re.fullmatch(pattern,date):
            wynikowa_lista.append(date)
    
    return wynikowa_lista
          
if __name__ == "__main__":
    dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
    print(f(dates))