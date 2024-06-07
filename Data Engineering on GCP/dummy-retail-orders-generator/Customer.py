class Customer:
    def __init__(self, customer_id, first_name,last_name,email,gender,address, city, country):
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.gender=gender
        self.address=address
        self.city=city
        self.country=country

    def __dict__(self):
        d={
            "customerId":self.customer_id,
            "customerName":{"firstName":self.first_name,"lastName":self.last_name},
            "gender":self.gender,
            "contactDetails":{"email":self.email,
                "address":self.address,"city":self.city,"country":self.country}    
        }
        return d
    
    def _change_name(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def _change_adress(self, address, city, country):
        self.address=address
        self.city=city
        self.country=country
    
    def _change_gender(self, gender):
        self.gender=gender

    def _change_email(self, email):
        self.email=email        
        
#c1=Customer(1,"Avinash","Waghole","M","1811, 2550, Simcoe St N","Oshawa","Canada")

#print(c1.__dict__())
#c1._change_name("Avi","Waghole")
#print(c1.__dict__())
#c1._change_gender("Male")
#print(c1.__dict__())

