a = list(map(int, input().split()))
a.sort()
n = len(a)
b = a[::-1]
c = []
for i in range(n // 2):
    c.append(b[i])
    c.append(a[i])
x=0
for i in a:
    if i not in c:
        x = i
        c.append(x)
print(*c)
