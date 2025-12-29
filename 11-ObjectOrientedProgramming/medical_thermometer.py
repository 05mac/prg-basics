import random

class thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0
    def turnOn(self):
        self.is_on = True
        print("Thermometer has been turn on ")
    
    def turnOff(self):
        self.is_on = False
        print("Thermometer has been turn off ")

    def measureTemp(self):
        
        print("Wait...")
        temperature = round(random.uniform(34.0,42.0),1)
        self.temperature = temperature
        print(f"Your tempertaure is: {self.temperature}")
        
    def showStatus(self):
        if self.is_on:
            if self.temperature >= 37.0:
                print(f"Temperature: {self.temperature} (fever)")
            elif self.temperature >= 41.0:
                print(f"Temperature: {self.temperature} (CRITICAL TEMPERATURE)")
            elif self.temperature < 34.0:
                print(f"Twoja temperatura to: {self.temperature} chyba nie żyjesz")
        else:
            print("Thermometer is turn off, please turn it on to show status")
            