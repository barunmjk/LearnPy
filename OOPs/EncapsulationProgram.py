class Factory:
             __name='kia'
             
             def __init__(self,__tyre):
                     self.__tyre=__tyre
             def getDetails(self):
                     print(f'car is {self.__name} and tyre is{self.__tyre}')  

obj=Factory('MRF')
obj.getDetails()
                                       