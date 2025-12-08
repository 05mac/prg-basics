class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Distance is: ', self.distance)
        print(f'Rate: ', self.rate_per_km)
        print(f'Fare is: ', self.fare)



def main():
    # your program
    taxiride1 = TaxiRide(5)
    taxiride1.calculate_fare(500)
    taxiride1.print_receipt()

    taxiride2 = TaxiRide(3)
    taxiride2.calculate_fare(230)
    taxiride2.print_receipt()

if __name__ == "__main__":
    main()
