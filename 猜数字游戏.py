import random

while True:
    print("----- 新一局猜数字游戏 -----")
    answer = random.randint(1, 100)
    while True:
        guess = int(input("请猜1-100的数字： "))
        if guess < answer:
            print("小了")
        elif guess > answer:
            print("大了")
        else:
            print("恭喜你答对了！")
            break
    choice = input("再来一局吗？ 输入 y 继续，其他退出： ")
    if choice != 'y':
        print("游戏结束！")
        break