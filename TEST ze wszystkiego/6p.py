class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        napis = ""
        if self.age >= 18:
            napis  += self.surname
            napis  += self.name[0]
            napis  += str(self.seniority)
            str(napis)

            return f"{napis.upper()}"
        
        if self.age <= 18:
            napis  += self.surname
            napis  += self.name[0]
            napis  += str(self.seniority)
            str(napis)

            return f"{napis.lower()}"
        

if __name__ == "__main__":
    print(C("Anna","May",17,7))
    print(C("George","Brown",21,4))