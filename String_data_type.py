# Define a String

s1= "welcome to Python Learning"

print(s1)

# Update a String

#s1[10]="T"  Doesnot Support

#Print the length of the String

print(len(s1))

#print an element of the String

print(s1[11])

#print a part of the String

print(s1[0:8])

#Locate a character in a String
print(s1.index('o'))

#Count a character that number of times repeated in a string

c=s1.count('e')
print(c)

c1=s1.count('e',0,10)
print(c1)

#Reverse the String
r=s1[::-1]
print(r)

r1=s1[1:-2]
print(r1)


# Convert the entire string to  Upper case

u1=s1.upper()
print(u1)



#Convert the entire string to lower case

l1=u1.lower()
print(l1)
#Concatination of String

c1= u1+" "+l1 + ' Aadvik'

print(c1)


#Print the String multiple times

print('Aadvik ' *3)

print(len(s1))
print(s1.center(160,"-"))

print("The sum of 2+3 is {1} and multiply of 2*3 is {0}".format(2*3,2+3))

