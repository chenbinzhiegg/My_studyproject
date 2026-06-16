import math_operations as op

operation_symbols = ["+","-","*","/","^","!"]

print("这是一个运算程序")
print("需要输入两个数a,b来进行运算")
print("提示:若求a的阶乘(a若非整数将被自动四舍五入),则b为任意数均可\n")


while True:
    a = input("请输入第一个数： a=")
    b = input("请输入第二个数： b=")
    s = input("请输入操作符（+、-、*、/、^、!): ")

    if s not in operation_symbols:
        print("无效的操作符") 
        continue
    
    try:
        a=float(a)
        b=float(b)
        break
    except :
        print("输入的不是数字")
        continue
    
if s == "+":
        r = op.add(a,b)
        print(f"{a}+{b}的结果为：{r}")
if s == "-":
        r = op.subtract(a,b)
        print(f"{a}-{b}的结果为：{r}")
if s == "*":
        r = op.multiply(a,b)
        print(f"{a}*{b}的结果为：{r}")
if s == "/":
        r = op.divide(a,b)
        print(f"{a}/{b}的结果为：{r}")
if s == "^":
        r = op.power(a,b)
        print(f"{a}的{b}次方是：{r}")
if s == "!":
    if a <0 :
        print("负数无法进行阶乘！")
    else :
        a = int(a)
        r = op.factorial(a)
        print(f"{a}的阶乘为：{r}")

	

