class Student:
    name="Grace"
    age=20
    school="AkiraChix"
    nationality="Kenyan"

class Students:
    school="AkiraChix"   
    def __init__(self,name,age,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality
    def greet_student(self): 
        return f"Hello {self.name} welcome to {self.school}"
    def year_of_birth(self):
        year=2023-self.age
        return f"Hello {self.age}, you were born in {year}"
    
    
    
class Product:
    def __init__(self,name,price,category,stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        
    def restock_product(self,amount):
        self.stock += amount
        print(self.stock)
        
    def sell(self,amount):
        if amount <= self.stock:
            self.stock -= amount
            print(f"{amount}  {self.name} are available")
        else:
            print(f"{self.name} is out of stock to sell {amount}")
            
    def view(self):
        print(f"Name:{self.name}")
        print(f"Name:{self.price}")
        print(f"Name:{self.category}")
        
# mango = Product(name="mango",price=45,category="fruits")
# orange = Product(name="orange",price=50,category="fruits")
# kales = Product(name="kales",price=60,category="vegetables")



class Delivery:
    def __init__(self,order,delivery_options,status="pending"):
        self.order = order
        self.delivery_options=delivery_options
        self.status = status
    def update_status(self,new_status):
        self.status = new_status
    def view_info(self):
        print("Delivery status")
        print(f"Order ID: {self.order.ID}")
        print(f"Customer Name: {self.order.customer.name}")
        print(f"Driver Name:{self.driver.name}")
        print(f"Status:{self.status}")
        
        
        
class Order:
    def __init__(self, deliveryOptions):
        self.deliveryOptions = deliveryOptions
    
    def getDeliveryOptions(self):
        return self.deliveryOptions

order = Order( [ "Home Delivery", "Pickup point"])
deliveryOptions = order.getDeliveryOptions()
print(deliveryOptions)
            
                    
        