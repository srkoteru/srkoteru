s = "ABC"
n = len(s)-1
d = [""] * (n+1)
li = list(s)
index = 0

def strrep(li,index,n):
    
    if(index== n):
        print("".join(li))
    else:        
        for i in range(n):
            d[index]= li[i]
            strrep(li,index+1,n)
    
    
    


strrep(li,index,n)
#print(count)
        
         