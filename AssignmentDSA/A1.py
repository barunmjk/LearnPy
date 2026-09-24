#print all positive and naegative  element separately
#input :[3,-1,4,-5,9] positive :[3,4,9] negative:[-1,-5]


l=[3,-1,4,-5,9]
pos=[]
neg=[]
for i in l:
           if i>0:
                 pos.append(i)
           else :
                 neg.append(i)

print(pos)
print(neg)                 
                         

