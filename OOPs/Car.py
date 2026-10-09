class Engine:
        def __init__(self,weight,hp):
                self.weight=weight
                self.hp=hp

class Frame:
        def __init__(self,seat,bonut):
                 self.seat=seat 
                 self.bonut=bonut
class Car(Engine,Frame):  #multipleInheritance
                 def __init__(self, weight, hp,seat,bonut):
                            Frame.__init__(self,seat,bonut)
                            Engine.__init__(self,weight,hp)        
obj=Car('150kg','10hp',4,1)
print(obj.weight) 
print(obj.hp)                                                 
print(obj.seat) 
print(obj.bonut) 
                