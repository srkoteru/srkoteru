# Define a Set
l=('a','d','a','s','r','a',1,10)
print(l)
s=set(l)
print(s)
s1={'q','s','q','a',10,'a',"s"}
print(s1)

i1={1,4,2,7,5,9,1}
print(i1)
#count

i2={4,6,3,0,1}
print(i2)

# Union of sets

u=i1 | i2
#print(u)
#Intersection
i=i1 & i2
#print(i)

#Difference
d1=i1 - i2
#print(d1)
d2=i2 - i1
#print(d2)
#Semitric difference

s= i1 ^ i2
print(s)