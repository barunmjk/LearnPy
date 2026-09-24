#Check the plindrom String or not
def rev(s):
           word=''
           for i in range(len(s)-1,-1,-1):
                                          word=word+s[i]
           return word


str=input('Enter the String-:')  
res= rev(str) 
if(str==res):
             print('Number is palindrome')
else :
      print('number is not palindrome')             
