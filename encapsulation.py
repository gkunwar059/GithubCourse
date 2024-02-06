# private attributes __id

class Bookseller:
    
    def __init__(self,title,author,price,quantity):
        self.title=title
        self.author=author
        self.price=price
        self.quantity=quantity
        self.__discount=None
        
        
    def __repr__(self):
        return f"Book_title:{self.title},Book_author:{self.author},Book_price:{self.price},Book_Quantity:{self.quantity}"
    
    
    def set_discount(self,discount):
        self.__discount=discount


        
    def get_discount(self):
        if self.__discount:
            return self.price*(1-self.__discount)
        return self.price
        
        

book1=Bookseller("Karnali blue","Ganesh kunwar",450,100)
print(book1.set_discount(0.20))
print(book1.get_discount())
