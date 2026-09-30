l= ['a','d','f','s','a','d','f']
d={}
for i in l:
          if i in d.keys():
                         d[i] +=1
          else:       
               d[i] = 1
for i in d:
           print(f'{i} is present in {d[i]} times ')               