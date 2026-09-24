#print the factoe 12 =1,2,3,4,6,12

n=int(input('enter the number:-'))
stop=(n//2)+1
for i in range(1,stop):
         if n % i == 0 :
                 print(f'{i} is the factor')
          