# 1
from datetime import date, timedelta
# print("5 days ago it was:", date.today() - timedelta(5))

# 2
# print("Yesterday it was:", date.today() - timedelta(1))
# print("Today it is:", date.today())
# print("Tomorrow it will be:", date.today() + timedelta(1))

# 3
from datetime import datetime, time
# print(datetime.today().replace(microsecond=0))

# 4
# d1 = datetime.now()
# s = input("Write your date in format: '%Y-%m-%d %H:%M:%S': ")
# d2 = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
# timedelta = d1 - d2
# print(timedelta.days * 24 * 3600 + timedelta.seconds, "in seconds.")

# 2023-02-15 01:00:00
