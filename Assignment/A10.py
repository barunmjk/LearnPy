#Reverse a string without using built-in function---python ->nohtyp

def reverseSt(s) :
               word=''
               for i in range(len(s)-1,-1,-1):
                       word= word + s[i]
               return word             
                                
 
str = input('Enter the String :-') 
result=reverseSt(str)   
print(result)                   