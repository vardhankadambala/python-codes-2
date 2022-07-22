a=input()
b=a.split()
l=[]
s="aeiouAEIOU"
for i in b:
    c=i[1:]+i[0]
    l.append(c)
for i in l:
    if i[0] in s:
        x=i+'ay'
        print(x,end=" ")
    else:
        x=i+"ed"
        print(x,end=" ")
