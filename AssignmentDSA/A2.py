#print greatest element with index

l=[12,45,25,25,67,78,89,98]
g=0
idx=0
for i in range(len(l)):
                       if g<l[i]:
                                g=l[i]
                                idx=i

print(f'Greatest element:{g} and index is {idx}')



                                  