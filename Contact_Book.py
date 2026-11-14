class Contact:
    def __init__(self, contact_id,name,phone_number):
        self.id=contact_id
        self.name=name
        self.phone_number=phone_number
    def __str__(self):
            return f"ID:{self.id} NAME: {self.name} PHONE NUMBER: {self.phone_number}"
            
               
        
class ContactBook:
    def __init__ (self):
        self.contact_list=[]
        
    def add(self, contact):
        for saved_contact in self.contact_list:
            
            
            if (saved_contact.name).upper() == contact.name.upper():
                return "contact alredy exist"
        
        self.contact_list.append(contact)
        return"Contact added"
    
    def search(self,name):
        for search_contact in self.contact_list:
            if search_contact.name.upper()==name.upper():
                return search_contact
            
        return "contact not found"
    
    def delete(self,contact):
        for delete_contact in self.contact_list:
            if delete_contact.name.upper()==contact.upper():
                self.contact_list.remove(delete_contact)
                return 'Contact Delete'
        return"contact not found"
    
    def show_all(self):
        if not self.contact_list:
             print("This list is empty")   
        for all_contact in self.contact_list:
           print (all_contact)
               
      
            
        
contact=Contact("011226", "Karl", "770-987-9876")
book=ContactBook()
new=book.add(contact)
contact1=Contact("029384", 'Max', '475-374-8689')
new2=book.add(contact1)
new1=book.show_all()

