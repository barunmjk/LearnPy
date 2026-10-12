from abc import ABC ,abstractmethod

class enforce(ABC):
       @abstractmethod
       def startEngine():
              pass

class Scooty(enforce):
      def startEngine():
                    pass
class Bike(enforce):
      def startEngine():
                    pass
class Car:
      pass

obj =Scooty()
obj2=Bike()
obj3=Car()