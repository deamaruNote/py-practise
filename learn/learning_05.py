###################################### 
# 模組 module 使用
# 內建模組可以查 python module list 

# import tool
# import token as tk # 改名
# import sys
# 
# ans = tool.max_num(2,3,4)
# 
# print(ans)
# 
# print(sys.path)  # 列出嵌入的模組位置


###################################### 
######  類別 class 、 物件 object #####
class Phone:
    def __init__(self, os, number, is_waterproof): #self->物件本身
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
    
    def add(self, num1, num2):
        return num1 + num2

###### 繼承
class Apple(Phone):
    def __init__(self, os, number, is_waterproof, member_mail):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
        self.member_mail = member_mail
        # super().__init__(os, number, is_waterproof)

phone1 = Phone("ios", 123, True)
apple1 = Apple("ios", 123456, True, "aaa@apple.com")


print("#############")
print(phone1.is_ios())
print(phone1.add(5,6))
print("#############")
print(apple1.is_ios())
print(apple1.member_mail)