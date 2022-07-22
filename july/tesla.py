t=int(input())

for i in range(t):
    x=0
    f,b,t,d=map(int,input().split())
    while b<d:
        x+=(f+b)*t
        d=d-(b-f)
    x+=d*t

    print(x)

