from datetime import datetime
from datetime import timedelta
t=int(input())
for i in range(t):
    x,Begindatestring = map(str,input().split())
    y=int(x)
    Begindate = datetime.strptime(Begindatestring, "%m/%d/%Y")
    Enddate = Begindate + timedelta(days=y)
    print(Enddate.month,end="/")
    print(Enddate.day,end="/")
    print(Enddate.year)