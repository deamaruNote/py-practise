# 日期
import calendar
from datetime import datetime

now = datetime.now()

yy = now.year
mm = now.month

print(calendar.month(yy,mm))