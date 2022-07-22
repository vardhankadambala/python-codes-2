def reverse(a):
    i = 0
    while a != 0:
        i = i * 10 + a % 10
        a = a // 10
    return i

a=int(input())
while True:
    if a==reverse(a):
        print(a,"pallen")
        break
    else:
        a=a+reverse(a)


