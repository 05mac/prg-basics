## magazyn danych
class Contact_list:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self,contact_object):
        self.contact_object = contact_object
        self.contacts.append(self.contact_object)
    
    def display_info(self):
        print("Kontakty")
        for person in self.contacts:
            print(person)