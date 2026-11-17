import random  # 导入 random 模块，用于生成随机数

while True:  # 外层循环：控制“是否再来一局”，每轮代表一整局游戏
    print("----- 新一局猜数字游戏 -----")  # 打印一局开始的分隔提示
    answer = random.randint(1, 100)  # 随机生成 1-100 之间的整数作为本局答案
    while True:  # 内层循环：玩家反复猜测，直到猜中为止
        guess = int(input("请猜1-100的数字： "))  # 读取玩家输入并转换为整数
        if guess < answer:  # 猜的数字比答案小
            print("小了")  # 提示“小了”
        elif guess > answer:  # 猜的数字比答案大
            print("大了")  # 提示“大了”
        else:  # 既不小也不大，说明猜中了
            print("恭喜你答对了！")  # 提示猜中
            break  # 跳出内层循环，结束本局猜测
    choice = input("再来一局吗？ 输入 y 继续，其他退出： ")  # 询问玩家是否再来一局
    if choice != 'y':  # 输入不是小写 y
        print("游戏结束！")  # 提示游戏结束
        break  # 跳出外层循环，程序退出
