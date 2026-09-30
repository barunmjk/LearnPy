#merge two dictionary  
d1 ={'a':10 ,'b':20}
d2={'b':30,'c':40,'d':60}

for i in d2:
            d1[i]=d2[i]

print(d1)