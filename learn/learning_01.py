age = 123
str(age)               # -> "123"

# -----------------------> list 列表
scores = [90,50,40,100]
friends = ["123",123,456,"Hello"]

#
len(scores)            # printf(..) -> 4

#更改
scores.clear()         # scores -> []
scores.extend(friends) # scores -> [90,50,40,100,"123",123,456,"Hello"]
scores.pop()           # scores -> [90,50,40]
scores.remove(40)      # scores -> [90,50,100]
scores.insert(2,10)    # scores -> [90,50,40,10,100]
scores.append(56)      # scores -> [90,50,40,100,56]

#排序
scores.sort()          # scores -> [40,50,90,100]
scores.reverse()       # scores -> [100,40,50,90]

#搜尋
scores.index(90)       # print(..) -> 0 回傳第一個找到的
scores.count(90)       # print(..) -> 1 回傳有多少個結果


# -----------------------> tuple 元祖: 不能做新增/修改/刪除
scores = (90,80,40,50,60)
scores[0:2]            # -> (90, 80)



# -----------------------> function 函式: 先定義再呼叫
def hello(name, school):
    print("hello" + name + "就讀" + school)
    return None        # 可寫可不寫

hello("No!", "某某小學")

def add(num1, num2):
    sum = num1 + num2
    return sum

add(5, 10)             # -> 15

# -----------------------> if 判斷句
types = True
if types and types == 4:
    print("以及...") 
elif types == 123 or types == 456:
    print("或者...")
elif not(types):
    print("types 為非") # types != 100 不等於
else:
    print("other...")


# -----------------------> 字典dictionary
#   key value
#   鍵   值

dic = {
    "apple": "蘋果",
    "banana": "香蕉",
    "cat": "貓"
}
dic("apple")       # -> 蘋果

# -----------------------> while 迴圈

i = 5
while i<= 5:
    print(i)
    i += 1

print("end")

# 1 2 3 4 5 end

# -----------------------> for 迴圈

for i in range(100):
    print("> " + i)
# 0 1 ... 99

for i in range(1, 10):
    print("> " + i)
# 1 ... 9

for letter in "大家好":
    print(letter)
# 大 家 好

for num in [0,2,4,6,8,10]:
    print(num)
# 0 2 4 6 8 10



