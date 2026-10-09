class ElectonicDevice:
                      def __init__(self,name):
                              self.name=name

class Laptop(ElectonicDevice):
                                pass
obj=ElectonicDevice('Mobile')
obj2=Laptop('dell')
print(obj2.name)

