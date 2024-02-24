#Ex1

import datetime

x = datetime.datetime.now()
y = datetime.timedelta(days = 5)
print(x-y)
#i undestand like this

#Ex2

z = datetime.datetime.now()
w = datetime.timedelta(days=1)
print("Yesterday:", z - w)
print("Today:", z)
print("Tomorrow:", z + w)

#Ex3

from datetime import datetime

q = datetime.now()
print(q.replace(microsecond=0))

#Ex4

a = datetime.now()
b = datetime(2024, 2, 20, 5, 19, 21, 150339)
print(int(a.strftime("%S")) - int(b.strftime("%S")))