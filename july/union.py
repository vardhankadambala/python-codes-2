a=int(input())
b=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
for i in a2:
    if i not in a1:
        a1.append(i)
a1.sort()
print(*a1)
