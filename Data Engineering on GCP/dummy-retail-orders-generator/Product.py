class Product:
    def __init__(self,product_id, product_name,category_id,category_name,rate,quantity=1):
        self.product_id=product_id
        self.product_name=product_name
        self.category_id=category_id
        self.category_name=category_name
        self.rate=rate
        if not quantity:
            self.quantity=1
        else:
            self.quantity=quantity
    
    def _set_quantity(self, quantity):
        self.quantity=quantity
        
    def __dict__(self):
        d={
            "productId":str(self.product_id),
            "productName":self.product_name,
            "category_id":str(self.category_id),
            "category_name":self.category_name,
            "rate":str(self.rate),
            "quantity":str(self.quantity)
        }
        return d
    
#p=Product(1,'A',2,"AA",10,2)
#print(p)    
