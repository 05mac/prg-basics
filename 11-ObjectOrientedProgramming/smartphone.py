from contact_list import Contact_list
from contact import Contact

my_contacts = Contact_list()

person1 = Contact("John Brown","brown@onet.pl","555234000")
person2 = Contact("Anna May","am@o2.pl","235234000")
person3 = Contact("George Small","smallg@google.pl","662234000")
person4 = Contact("Paola Big","bigpaola@poczta.pl","987334000")

my_contacts.add_contact(person1)
my_contacts.add_contact(person2)
my_contacts.add_contact(person3)
my_contacts.add_contact(person4)

my_contacts.display_info()


