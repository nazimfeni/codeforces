#25A IQ Test
n=int(input())
if(n<3 or n>100):
    print("Input valid number in range")
else:
    li=[]
    li=input().split()
    even=0
    odd=0
    j=0
    while (j<n):
        if(int(li[j])%2==0):
            even+=1
        else:
            odd+=1
        j+=1

    k=0

    if(odd==1):
        while(k<n):
            if(int(li[k])%2!=0):
                print(k+1)
                break
            k+=1 
    
    if(even==1):
           while(k<n):
            if(int(li[k])%2==0):
                print(k+1)
                break
            k+=1 
        
