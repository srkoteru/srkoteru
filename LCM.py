l1= input("enter the list of elements:")
l= l1.split(",")
lcm = int(min(l)) * int(max(l))
i = 0

while(i <len(l)):
        if (lcm % int(l[i])!= 0):
            lcm= lcm + int(max(l))
            i = 0
        else: 
            i= i+1
 
            
print ("LCM of the given list of elements {0} is :{1}".format(l,lcm))
        
    






