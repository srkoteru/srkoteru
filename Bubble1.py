a = [2,9,3,6,29,14,68,24,29,99,72]

n = len(a)

def swap(a,i,):
    temp = a[j]
    a[j] = a[j+1]
    a[j+1] = temp
    
for i in range(n):
    for j in range(n-i-1):
        if (a[j] > a[j+1]):
            swap(a,j)

print(a)
