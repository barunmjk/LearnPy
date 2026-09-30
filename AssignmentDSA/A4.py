#sort the list

l = [12, 45, 9, 56, 78, 89, 67]

for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):

        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp

print(l)                                        
 