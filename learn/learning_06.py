# 問答程式
from question import Question  # 只引入某個 ...

test = [
    "1+3=?\n (a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於多少公分?\n (a) 100\n (b) 89\n (c) 10\n\n",
    "蘋果是什麼顏色?\n (a) 黃色\n (b) 紅色\n (c) 黑色\n\n"
]

questions = [
    Question(test[0], "c"),
    Question(test[1], "a"),
    Question(test[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score = score +1
    
    print("你得到:" + str(score) + "分，共" + str(len(questions)) + "題")

run_test(questions)
