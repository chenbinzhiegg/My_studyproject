"""
练习题：输入学生信息，判断成绩等级并存储至列表
需求：
1. 输入姓名、年龄、分数
2. if分支判断分数对应等级:
    90-100 A
    80-89  B
    70-79  C
    60-69  D
    <60     E
3. 把全部信息存入列表并打印
"""

name=input("学生的姓名：")
age=int(input("年龄："))
grade=float(input("成绩："))
rank='E'

if grade>=90:
    rank='A'
elif grade>=80:
    rank='B'
elif grade>=70:
    rank='C'
elif grade>=60:
    rank='D'
else:
    rank='E'

student=[name,age,grade,rank]

print(f"学生{student[0]}的成绩为{student[2]}等级为{student[3]}")    #列表只能按位置索取，按名字索取应该要用dic
print("完整学生信息列表",student)

"""
得分：85/100
优点：
1. 功能完整，if判断区间无遗漏、逻辑正确
2. 变量命名清晰，使用f-string格式化输出可读性好
待优化点：
1. age未用int()转换，数据类型不规范
2. if条件多余括号，不符合Python书写习惯
3. 未打印完整学生信息列表，未完成题目全部要求
"""