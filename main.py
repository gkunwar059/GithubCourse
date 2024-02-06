class Mapping:
    def __init__(self,iterable) :
        self.items_list=[]
        self.__update(iterable)
        
    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)
            
    __update=update   #private copy of original update() method
    
class MappingSubClass(Mapping):
    def update(self,keys,values):
        for item in zip(keys,values):
            self.items_list.append(item)
        













# # 
# class Bag:
#     def __init__(self):
#         self.data=[]
        
#     def add(self,x):
#         self.data.append(x)
    
#     def add_twice(self,x):
#         # self.add(x)
#         self.add(x)