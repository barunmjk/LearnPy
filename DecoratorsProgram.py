def myDecorators(func):
                       def getGenz(*a,**b):
                                   print('hi genZ')
                                   print('we born after 1997')
                                   func(*a,**b)
                                    
                       return getGenz           
@myDecorators
def genAlpha():
               print('after genZ we born')

genAlpha()                                                  