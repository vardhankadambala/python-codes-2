n=int(input())
l=[]
for i in range(n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
print(*l)
s=0
for k in l:
    x=0
    s=str(k)
    l1=list(s)
    for m in l1:
        x=x+int(m)
        if x in l:
            print(k)