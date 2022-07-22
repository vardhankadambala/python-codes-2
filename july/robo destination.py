from itertools import permutations
m, n = map(int, input().split())
x, y = map(int, input().split())
a, b = map(int, input().split())
l = []
while x != a or y != b:
    if x > a:
        x = x - 1
        l.append("r")
    elif x < a:
        x = x + 1
        l.append("l")

    if y > b:
        y = y - 1
        l.append("u")
    elif y < b:
        y = y + 1
        l.append("d")
x=permutations(l)
for i in x:
    print("".join(i))
