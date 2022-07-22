#  *
#  #*
#  #*#
#  *#*#

n=int(input())
count=1
for i in range(n):
    for j in range(i+1):
        if count%2==0:
            print("#",end="")
        else:
            print("*",end="")
        count+=1
    print("")