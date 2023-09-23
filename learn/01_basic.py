import time

price = 123
check = isinstance(price, int)
check2 = type(price)
print(check, check2)

username = input('請輸入')
print(username)

###############################
year = input('Birth Year: ')
month = input('Birth Month: ')
date = input('Birth Day: ')
birth = year + '-' + month + '-' + date

now = int(time.time())
struct_now = time.localtime(now)
string_time  = time.strftime("%Y-%m-%d", struct_now)
string_year = time.strftime("%Y", struct_now)

result = int(string_year) - int(year)
print("年紀: ", str(result))