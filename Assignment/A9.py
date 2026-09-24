# number is perfect or not
 
def isPerfect(n):
             sum=0
              
             for i in range(1,n//2+1):
                  if n%i==0:
                        sum +=i

             return sum                  

n = int(input('Enter the number :- '))
num =n
sum=isPerfect(n)
if sum==num:
         print(f'Number is perfect is {sum}')
else:
        print('Number is not perfect') 
       
        
         
