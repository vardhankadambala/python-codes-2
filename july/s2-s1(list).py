#using list
t=int(input())
for i in range(t):
    a=input()
    b=input()
    s1=list(a)
    s2=list(b)
    l=[]
    for i in s1:
        if i not in s2:
            l.append(i)
    print("".join(l))