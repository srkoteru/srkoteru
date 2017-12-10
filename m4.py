s = "ABC"
l= len(s)-1
data = [""]*(l+1)
index = 0
count = 0
def srec(s,data,index,l):
    global count
    for i in range(l+1):
        data[index]= s[i]
        if (index==l):
            print("".join(data))
            count = count +1
        else:
            srec(s,data,index+1,l)   

srec(s,data,index,l)



print (count)
    
    