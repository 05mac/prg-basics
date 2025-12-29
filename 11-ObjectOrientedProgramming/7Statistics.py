class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers

    def display_numbers(self):
        for element in self.numbers:
            print(f"{element}, ")

    def greatest(self):
        self.najwieksza = self.numbers[0]
        for element in self.numbers:
            if element > self.najwieksza:
                self.najwieksza = element
        return self.najwieksza

    def smallest(self):
        self.najmniejsza = self.numbers[0]
        for element in self.numbers:
            if element < self.najmniejsza:
                self.najmniejsza = element
        return self.najmniejsza
    def arithmeticMean(self):
        self.sredniaArytmetyczna = 0
        sumaTablicy = sum(self.numbers)
        arthimeticMean = sumaTablicy / len(self.numbers)
        self.sredniaArytmetyczna = arthimeticMean

    def median(self):
        n = len(self.numbers)
        for i in range(n):
            for j in range(n):
                if self.numbers[i] < self.numbers[j]:
                    self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]

        wyrazSrodkowy = (int(n/2))
        if n % 2 == 0:
            self.mediana = ((self.numbers[wyrazSrodkowy] + self.numbers[wyrazSrodkowy - 1]) / 2)
        else:
            self.mediana = (self.numbers[wyrazSrodkowy])

    def __str__(self):
        return f"minimum: {self.smallest()}, maxiumum: {self.greatest()}, arithmetic mean: {self.sredniaArytmetyczna}, mediana: {self.mediana}"


mojeLiczby = Statistics([12, 37, 6, 9, 17])
mojeLiczby.greatest()
mojeLiczby.smallest()
mojeLiczby.arithmeticMean()
mojeLiczby.median()
print(mojeLiczby)
