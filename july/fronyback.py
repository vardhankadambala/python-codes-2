a=input()
b=list(a)
temp=b[0]
b[0]=b[-1]
b[-1]=temp
c="".join(b)
print(c)
