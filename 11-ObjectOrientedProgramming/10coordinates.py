class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, limit):
        n = len(self.coordinates)
        self.limit = limit
        counter = 0

        for i in range(n):
            dlugosc = len(self.coordinates[i])
            if self.coordinates[i][0] > 0 and self.coordinates[i][-1] > 0:
                counter += 1
        return counter >= self.limit

koordynaty1 = C([[2, 3],
                [1, 8],
                [-6, 4],
                [3, -7]])

print(koordynaty1.m(3))
