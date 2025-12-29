class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        
    def __str__(self):
        napis = ""
        if self.age >= 18:
            napis += (self.surname.upper())
            napis += self.name[0].upper()
            napis += str(self.seniority)
        else:
            napis += (self.surname.lower())
            napis += self.name[0].lower()
            napis += str(self.seniority)
        return napis  
            
chujek = C("Anna","May",17,7)
chujek2 = C("George","Brown",21,4)

print(chujek)
print(chujek2)