#sum of factor 12 = 1,2,3,4,6,12,  
#sum=28
sum=0
n=int(input('enter the number'))
for i in range (1,n+1):
            if n%i==0 :
                    sum +=i
print(f'sum of all factor is {sum}')                    
