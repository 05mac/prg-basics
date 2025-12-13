class Phone():
    def __init__(self,marka ,model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji


    def wlacz_telefon(self):
        print("telefon się włączył!")

    def wylacz_telefon(self):
        print("telefon się wyłączyl :/")

    def display_info(self):
        print(f"Mój telefon jest marki: {self.marka}, a model to: {self.model}, natomiast rok prodkucji to: {self.rok_produkcji}")
    

telefon1 = Phone("xiaomi","S2",2023)   
telefon1.wlacz_telefon()
telefon1.wylacz_telefon()
telefon1.display_info()  


            