#using while loop print reminder 
def getRem(n):
              while n>0: 
                        print(n%10)
                        n//=10

n=int(input('Enter the Number:-'))
getRem(n)