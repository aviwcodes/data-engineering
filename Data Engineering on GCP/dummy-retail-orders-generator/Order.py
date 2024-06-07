class Order:
    def __init__(self,order_id,customer_id,order_date, delivery_date,products=None):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_date=order_date
        self.delivery_date=delivery_date
        if not products:
            self.products=[]
        else:
            self.products.append()

    def _change_delivery_date(self, delivery_date):
        self.delivery_date=delivery_date
    
    def _change_order_date(self, order_date):
        self.order_date=order_date
        
    def _add_product(self, product):
        self.products.append(product)
    
    def __dict__(self):
        d={
            "orderId":self.order_id,
            "CustomerId":self.customer_id,
            "orderDate":str(self.order_date),
            "deliveryDate":str(self.delivery_date),
            "orderedProducts":self.products
        }
        return d
        
#o1=Order(1,1,None,None,None)
#print(o1.__dict__())
#p1=Product(1,"Maggi","2")
#o1._add_product(p1.__dict__())
#print("After adding prodycts.....\n")
#print(o1.__dict__())
               
            
                                    