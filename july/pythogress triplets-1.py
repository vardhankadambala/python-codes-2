a = int(input())
b = list(map(int, input().split()))
flag = 0
for i in range(a - 1):
    for j in range(i + 1, a):
        x = (b[i] ** 2 + b[j] ** 2) ** 0.5
        if x in b:
            print(b[i], b[j], int(x))
            flag = 1
if flag == 0:
    print("No Triplets")
