# 创建一个包含正数、负数和零的列表
numbers = [-5, 0, 3, -1, 8, 0, 12]
# 使用for循环遍历列表
for num in numbers:
    # 检查数字是否为负数或零
    if num <= 0:
        continue  # 如果是负数或零，则跳过当前迭代
    # 如果数字是正数，则打印它
    print(num,end=',')


print("\n")
# 设定正确的用户名和密码
correct_username = "admin"
correct_password = "password"
# 初始化用户输入的用户名和密码
username = ""
password = ""
# 使用while循环来模拟登录过程
while True:  #一直循环，直到主动跳出(break)
    # 获取用户输入的用户名
    username = input("请输入用户名：")
    # 检查用户名是否正确
    if username != correct_username:
        print("用户名错误，请重新输入。")
        continue  # 用户名错误，跳过当前迭代，重新要求输入用户名;正确的话继续下一步
    # 获取用户输入的密码
    password = input("请输入密码：")
    # 检查密码是否正确
    if password != correct_password:
        print("密码错误，请重新输入。")
        continue  # 密码错误，跳过当前迭代，重新要求输入用户名和密码
    # 如果用户名和密码都正确，则登录成功
    print("登录成功！")
    break  # 跳出循环
# 登录成功后可以执行其他操作...