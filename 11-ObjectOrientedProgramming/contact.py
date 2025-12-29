class Contact:
    def  __init__(self,name,email,phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        
    def __str__(self):
        return f"{self.name:15}, {self.email:20}, {self.phone_number}"    
        
       