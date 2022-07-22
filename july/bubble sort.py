a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a):
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]
print(*b)
