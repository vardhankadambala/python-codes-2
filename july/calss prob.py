def sumdig(n):
    s = str(n)
    x = list(map(int, s.strip()))
    y = sum(x)
    if y > 10:
        sumdig(y)
    else:
        return y


a = int(input())
l = []
for i in range(a):
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            l.append(i)

for n in l:
    y = sumdig(n)
    if y in l:
        print(n, end=" ")
