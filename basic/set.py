#set
s1={3,4,5}
print(10 in s1) #10是否在s1中?
s2={4,5,6,7}

s3=s1&s2 # 取s1跟s2的集合 共有的
s3=s1|s2 # 取s1跟s2的聯集 全部都有但不重複
s3=s1-s2 # 差集:從s1中，減去和s2重疊的部分
s3=s1^s2 # 反交集，取不重疊的部分

s3=set("Hello") #變成{"H", "e", "l", "l", "o"}

#dictionary
dic={"apple":123,"banana":456}
print(dic['apple'])
print("apple" in dic)  #尋找key值
del dic["apple"] #刪除apple的key值


#
#
#
###############
dic={x:x*2 for x in [3,4,5]}
#列印為 {3:6, 4:8, 5:10}
 