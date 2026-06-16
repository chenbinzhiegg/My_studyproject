import random

print("你好！这是一个猜数字的游戏，快输入一个0~100之间的数来试试吧！")
number_list=[1,13,2,26,9,18,10,28,4,8]
i = 0

ran_data = random.choice(number_list)

while True:
    user_data = input("\n请输入你猜的数字：")
    try:
        user_data = int(user_data)
        if user_data in number_list :
            if user_data == ran_data :
                print("恭喜你，猜对了！")
                break
            else:
                print("猜错了，再试试吧！")
                i = i+1
                continue
        else:
            print("这个数字不在列表当中，请重新输入")
            i = i+1
            continue
    except:
        print("您输入的数据类型有误，请输入整数。")

if i == 0 :
    print("厉害，一次就猜对了！")
else:
    print(f"\n你一共猜错了{i}次，欢迎继续挑战！")