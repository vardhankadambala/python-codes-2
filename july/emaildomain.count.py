a=int(input())
x="xsidcz.xyz"
l=[]
for i in range(a):
    b=input()
    l.append(b)
m=[]
for i in l:
    if x in i:
        m.append(i)
print(len(m))