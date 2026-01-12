import math
class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        cwiartka = 0
        cwiartka_2 = 0
    def m1(self):
        if self.x == 0 or self.y ==0:
            self.cwiartka = 0 
        
        # 1

        if (self.x > 0 and self.y > 0):
           self.cwiartka = 1 
        
          # 2

        if (self.x < 0 and self.y > 0):
           self.cwiartka = 2
        
          # 3

        if (self.x < 0 and self.y < 0):
           self.cwiartka = 3
        
          # 4

        if (self.x > 0 and self.y < 0):
           self.cwiartka = 4
    
        return self.cwiartka
    
    def m2(self,a,b):
        self.a = a
        self.b = b

        if self.a == 0 or self.b ==0:
           self.cwiartka_2 = 0 
        
        # 1

        if (self.a > 0 and self.b > 0):
           self.cwiartka_2 = 1 
        
          # 2

        if (self.a < 0 and self.b > 0):
           self.cwiartka_2 = 2
        
          # 3

        if (self.a < 0 and self.b < 0):
           self.cwiartka_2 = 3
        
          # 4

        if (self.a > 0 and self.b < 0):
          self.cwiartka_2 = 4
    
        return self.cwiartka_2 == self.cwiartka
    
    def m3(self,a,b):
       self.a = a
       self.b = b

       distance = math.sqrt((self.a - self.x)**2 + (self.b - self.y)**2)

       if distance > 5:
          return True
       else:
          return False
if __name__ == "__main__":
    p = C(2,3)
    print(p.m1())
    print(p.m2(7,4))
    print(p.m2(-3,1))
    print(p.m3(8,5))
    print(p.m3(4,7))
    print("-----------------")
    p1 = C(0,5)
    print(p1.m1())
    print(p1.m2(4,7))
    print(p1.m2(-7,0))
        