import random
comGess=random.randint(1,100)
step=0
 
while True:
           userGess=int(input('Enter Your Guess Number--:'))
           if comGess==userGess:
                     print('Congrat you win....')
                     step+=1
                     break
           elif comGess>userGess:
                      print('Sorry Wrong Guess number is higher')
                      step+=1
           elif comGess<userGess:
                      print('Sorry Wrong Guess number is lower')                   
                      step+=1

print('Step is ',step)