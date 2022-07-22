#using string
t=int(input())
for i in range(t):
    a=input()
    b=input()
    for i in a:
        if i not in b:
            print(i,end="")0