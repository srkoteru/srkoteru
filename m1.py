l1= input("enter the list of elements:")
l = l1.split(',')
s = set(l)

if(len(s) == len(l)):
    print(" there is no duplicates")
else:
    print( "duplicates  are there")