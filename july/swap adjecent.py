a=list(map(int,input().split()))
x=0
l=[]
while x<len(a):
    temp=a[x]
    a[x]=a[x+1]
    a[x+1]=temp
    # l.append(a[x])
    print(a[x],a[x+1],end=" ")
    # l.append(a[x+1])
    x=x+2
# print(l)

