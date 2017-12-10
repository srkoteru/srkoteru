a = [2,9,3,6,29,14,68,24,29,99,72,101,1,999]
n = len(a)-1
   
def insertrec(a,i,n):
    key = a[i]
    j = i-1
    while ((j >=0) and (key < a[j])):
        a[j+1] = a[j]
        j=j-1
    a[j+1] = key
    if (i < n):
        insertrec(a,i+1,n)

insertrec(a,1,n)
        
        
print(a)
            
            
    
    



