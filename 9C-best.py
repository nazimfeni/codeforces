# counting binary number in decimal range
# Developed by Nazim

li=[]
i=0;
while (i<=1024):
  y=list(bin(i))
  y.pop(0)
  y.pop(0)
  k=int("".join(x for x in y))
  li.append(k) # 1 to 512 binaray is apending li list
  i+=1 

n=int(input())
if((n<1) or (n>10**9)):
    print("Input the number in correct range")
else:
    l=len(str(n))
    s=(2**(l-1))
    j=1
    count=0
    while li[s+j]<=n:    
        if(li[l+j]==n):
            j=j+1
            count=count+1
            break
        else:
            count=count+1
            j=j+1
        
    print(s+count)

