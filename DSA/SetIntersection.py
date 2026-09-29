s1={10,20,30,40}
s2={30,40,50,60}
s3={30,40}
#s1=s1.intersection(s2)
#print(s1)
# same as in down 
#s1 &= s2
#print(s1)
#=====subset below====
#print(s3.issubset(s2))
#or
#print(s3<=s2)
#print(s2.issuperset(s3)) 
#or
#print(s2>=s3)

print(s1.symmetric_difference(s2))
print(s1|s2)
