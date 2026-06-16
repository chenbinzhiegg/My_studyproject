#  try:
# 尝试执行的代码块  
# 这里可能会引发异常  
#except ExceptionType1:
# 当 ExceptionType1 异常发生时执行的代码块  
#  except ExceptionType2 as e:
# 当 ExceptionType2 异常发生时执行的代码块，并且可以获取异常对象的信息  
#  else:
# 如果没有异常发生时执行的代码块  
#  finally:

while True:
    try:
      data=input(  "请输入数据："  )
      data=int(data)  
      sum=2+data  
      print(  "结果是："  ,  sum)
      break  
    except   ValueError:  
      print(  "您输入的数据不符合指定类型"  )


try:
    data = input("请输入数据：")  
    # 关键修改：将输入的字符串转为浮点数（兼容整数和小数）
    data_num = float(data)  
    sum_result = 2 + data_num  # 变量名避免用sum（Python内置函数）
    print("结果是：", sum_result)  
except ValueError:  # 捕获“值错误”（输入无法转为数字时触发）
    print("您输入的不是有效数字，请输入整数或小数")
except TypeError:   # 保留类型错误捕获（防御性处理）(数据类型不对，类型不匹配：你让两种不能一起运算 / 转换的数据类型做操作，Python 无法执行，抛出该错误。)
    print("您输入的数据不符合指定类型")