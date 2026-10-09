class ShoesFactory:
        def __init__(self,name,type):
                self.name=name
                self.type=type
        def getDetails(self):
                print(f'name of shoes is {self.name} and type is {self.type}')

class Nike(ShoesFactory):
        def __init__(self, name, type,size):
                super().__init__(name, type)
                self.size=size
        def getDetails(self):
                print(f'name of shoes is {self.name} and type is {self.type} and size is {self.size}') 

class Campus(Nike):
                  def __init__(self, name, type, size,price):
                          super().__init__(name, type, size)
                          self.price=price 

                  def getDetails(self):
                        print(f'name of shoes is {self.name} and type is {self.type} and size is {self.size} and price is {self.price}')
obj=Campus('Ultra','SportsShoe',32,8900.50)

print(obj.getDetails())
