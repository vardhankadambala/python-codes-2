from datetime import datetime
from datetime import timedelta
t=int(input())
for i in range(t):
    x,bs=map(str,input().split())
    Begin = datetime.strptime(bs, "%m/%d/%Y")
    End = Begin + timedelta(days=int(x))
    print(End)
