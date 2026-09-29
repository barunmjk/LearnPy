#print sencond largest element

l=[12,34,56,89,46,56,56]
lar=l[0]
idx=0
slarg=0
for i in range(len(l)):
                       if lar<l[i]:
                                   slarg=lar
                                   lar=l[i]
print(f'largest value is {lar} and second largest value is {slarg}')            

