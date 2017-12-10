a = [200,2,9,3,6,29,14,68,24,29,99,72,101,1,0,102]
n = len(a)
for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if(a[min] < a[j]):
            min = j
    a[i],a[min] = a[min],a[i]
    

print(a)
    

               
 
    
    



