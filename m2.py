s = str(input('Enter the string with out repeated chars:'))
li = list(s)
n =  len(li)
l = 0
r=n-1
count =  0
def swap(a,i,l):
    temp = a[i]
    a[i] = a[l]
    a[l] = temp
def permute(a,l,r):
    global count
    if(l == r):
        print("".join(a))
        count  = count + 1
    else:
        for i in range(l,r+1):
                swap(a,i,l)
                permute(a,l+1,r)
                swap(a,i,l)
            
                
            
permute(li,l,r)
print(count)