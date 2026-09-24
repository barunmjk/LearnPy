#number is prime or not
     
def isPrime(n):
    if n<=1:
        return False
    elif n==2 or n==3:
         return True 
    elif n%2==0:
              return False
    for i in range(3,n//2+1,2): 
                  if n%i==0:
                     return False
    return True              
             
n=int(input('Enter the number:'))
if isPrime(n):
       print('num is prime ')
else: 
     print('number is not prime')  