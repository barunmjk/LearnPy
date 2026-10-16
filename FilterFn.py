
l=[23,13,14,56,22,17]

def isPrime(n):
            if n<=1 :
                     return False
            elif n==2 or n==3:
                     return True
            elif n%2==0 :
                     return False
            for i in range(3,n//2+1,2) :
                     if n%i==0:
                              return False
            return True          

prime =list(filter(isPrime,l))

print(prime)