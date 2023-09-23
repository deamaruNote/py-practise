# 2維列表、巢狀迴圈

nums = [
    [1,2,3],
    [3,4,5],
    [6,7,8],
    [9]
]

nums[0][0] # |-> 1

# for row in nums:
#     for col in row:
#         print(col)


######################################
####       檔案讀取及寫入           ###

# open("檔案路徑", mode="開啟模式")

# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原先的衣料後寫東西 

# file = open("123.txt", mode="r")   | <===重要
# print(file.read())          #讀全部
# file.readline()             #讀單行
# print(file.readlines())     #讀全部，並以陣列表示
# file.close() 

# file = open("123.txt", mode="w")
# file.write("test\n 11111")    #覆寫 
# file.close() 


# file = open("123.txt", mode="a", encoding="utf-8")   #|<=== 加入編碼方式     
# file.write("test\n 11111")
# file.close() 

# 可自動關閉
with open("123.txt", mode="a", encoding="utf-8") as file:
    file.write("\n哈哈")