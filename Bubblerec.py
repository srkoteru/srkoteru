a = [2,9,3,6,29,14,68,24,29,99,72,101,1]
n = len(a)-1
def swap(a,i):
    
    a[i],a[i+1] = a[i+1],a[i]

def bubble(a,n): 
    for i in range(n):
        if(a[i] > a[i+1]):
            swap(a,i)
    if (n > 0):
        bubble(a,n-1)
       
bubble(a,n)
print(a)
