n=int(input())
a=list(map(int,input().split()))
# x=0
# for i in range(n):
#    x=x+1
#    print(x)
#    if x not in a:
#        print(x)
f=1
d=1
l=n+1
s=((l)*(2*f+(l-1)*d))/2
s1=sum(a)
print(int(s)-s1)