# 假设要查找数字5  
target_number = 5
# 循环遍历一个数字列表  
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    # 如果找到了目标数字  
    if number == target_number:
       # 使用break语句退出循环  
        print(f"找到了目标数字：{number}")
        break
    else:
        # 如果还没有找到，继续循环  
        print(f"当前数字是：{number}，但不是目标数字")
    # 如果循环正常结束（即没有通过break退出），则打印以下消息
else:
    print("未找到目标数字")

# 使用while循环进行密码验证
correct_password =111
print(correct_password)
verified = False
while not verified: #循环直到验证成功
    # 获取用户输入的密码
    password = int(input("请输入密码："))
    # 检查密码是否正确
    if password == correct_password:
        print("密码正确，验证通过！")
        verified = True  # 设置验证成功，退出循环
        #break  # 跳出循环
    else:
        print("密码错误，请重试。")