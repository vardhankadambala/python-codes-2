m, n = map(int, input().split())
x, y = map(int, input().split())
s = input()
l = list(s)
for i in range(len(l)):
    if l[i] == "l":
        x += 1
    elif l[i] == "r":
        x -= 1
    elif l[i] == "u":
        y -= 1
    elif l[i] == "d":
        y += 1
    else:
        print("give correct input in string")

if x>=0 and x<=m-1:
    if y>=0 and y<=n-1:
        print("yes")
else:
    print("no")
