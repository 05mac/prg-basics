import json

with open("reservations.json", "r", encoding="UTF-8") as plik:
    dane = json.load(plik)

numery_pokoi = []
liczba_oplaconych_rezerwacji = 0
liczba_NIEOPLACONYCH_rezeracji = 0
kwota_oplaconych_rezerwacji = 0
kwota_NIEPLACONYCH_rezerwacji = 0
for i in range(len(dane["reservations"])):
    numery_pokoi.append(((dane["reservations"][i]["room_number"])))
    if ((dane["reservations"][i]["paid"])):
        liczba_oplaconych_rezerwacji += 1
        kwota_oplaconych_rezerwacji += ((dane["reservations"][i]["nights"])) * (
            (dane["reservations"][i]["price_per_night"]))
    else:
        liczba_NIEOPLACONYCH_rezeracji += 1
        kwota_NIEPLACONYCH_rezerwacji += ((dane["reservations"][i]["nights"])) * (
            (dane["reservations"][i]["price_per_night"]))

print(f"Numeru pokoi: {numery_pokoi}, liczba oplaconych rezerwacji: {liczba_oplaconych_rezerwacji}, liczba nieoplaconych rezerawcji: {liczba_NIEOPLACONYCH_rezeracji}, kwota oplaconych rezerwacji: {kwota_oplaconych_rezerwacji}, kwota nieoplaconych rezerwacji: {kwota_NIEPLACONYCH_rezerwacji}")
