# Zadanie: Symulacja odbijającej się piłki (p2.py)Piłka zostaje upuszczona z wysokości początkowej $h_0$. Po każdym odbiciu od podłoża, piłka wznosi się na wysokość stanowiącą ułamek $r$ wysokości poprzedniej (współczynnik odbicia).Zdefiniuj funkcję f(h0, r, h), która obliczy i zwróci liczbę odbić piłki od podłoża, po których wysokość jej wzniesienia będzie wciąż większa niż zadany próg $h$.

def f(h0, r, h):
    counter = 0
    while h0 > h:
        h0 *= r
        counter += 1
    return counter


print(f(10, 0.8, 5))
print(f(10, 0.95, 5))
print(f(12, 0.7, 2))
