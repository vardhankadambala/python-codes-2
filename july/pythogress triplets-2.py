#pythogress thriplets:
a=int(input())
b=list(map(int,input().split()))
flag=0
for i in range(a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            x=b[i]*b[i]
            y=b[j]*b[j]
            z=b[k]*b[k]
            if x==y+z or y==x+z or z==x+y:
                print(b[i],b[j],b[k])
                flag=1
if flag==0:
    print("No Triplets")