l1 = input("enter the list of elements:")
l = l1.split(',')
i = 0
gcd = int(min(l))

for x in l: 
    if (int(x)% gcd != 0):
        gcd = round(gcd/2)
        break
    
if (gcd < int(min(l))):
     
     while(i < len(l)):
         if(int(l[i])% gcd != 0):
             gcd = gcd -1
             if(gcd <=1):
                 gcd= 1
             i = 0
         else:
             i= i+1 


    
print("GCD of the given list of numbers {0} is :{1}".format(l,gcd))




     

