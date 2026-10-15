#l=['mohan','sohan','rohan']

#length=list(map(len,l))
#print(length)

c=[0,3,2,32]

def convertFer(c):  
                f =(9/5*c)+32
                return f    
calfar=list(map(convertFer,c))
print(calfar)     