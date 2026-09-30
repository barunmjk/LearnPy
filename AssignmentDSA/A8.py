#print the frequency of number

l=[1,4,7,6,8,9,5,1,3,7,7]

d={}

for i in l:
          if i in d.keys() :
                        d[i]+=1
          else :
                  d[i]=1

for i in d:
           print(f'{i} is present in {d[i]} times')                  
