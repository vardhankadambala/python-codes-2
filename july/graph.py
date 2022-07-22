t=int(input())
x=[]
for i in range(t):
    l=list(map(int,input().split(",")))
    x.append(l)

print(*x)
