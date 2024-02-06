class Bookseller:
    def __init__(self,title,quantiy,author,price):
        self.title=title
        self.quantity= quantiy
        self.author=author
        self.price=price
        
        # 
    def __repr__(self):
        return f"Book:{self.title},Quantity:{self.quantity},Author:{self.author},Price:{self.price}"
        
book=Bookseller("Rich Dad",100,'Johana pardon',45000)
print(book)
        
# without this if we use this 
# <__main__.Book object at 0x00000156EE59A9D0>
# <__main__.Book object at 0x00000156EE59A8B0>
# <__main__.Book object at 0x00000156EE59ADF0>