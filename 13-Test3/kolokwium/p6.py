class C:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):

        napis = self.firstname[0] + self.lastname[0] + str(self.age)

        if self.age > 18:
            return napis.upper()
        else:
            return napis.lower()

if __name__ == "__main__":
    print(C("John","May",21))
    print(C("Anna","Brown",17))