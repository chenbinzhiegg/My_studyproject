#输入三个成绩，计算平均分，判断是否及格
#及格分数线常量
PASS_SCORE = 60

#获取学生成绩
grade1 = float(input("请输入第一科成绩: "))
grade2 = float(input("请输入第二科成绩: "))
grade3 = float(input("请输入第三科成绩: "))

#计算总分和平均分
total = grade1 + grade2 + grade3
average = total / 3

#判断及格还是不及格
if average >= PASS_SCORE:
    result = "及格"
else:
    result = "不及格"

#显示结果
print("=" * 30)
print("成绩报告单")
print("=" * 30)
print(f"第一科成绩: {grade1}")
print(f"第二科成绩: {grade2}")
print(f"第三科成绩: {grade3}")
print(f"总分: {total}")
print(f"平均分: {average:.1f}")
print(f"结果: {result}")
print("=" * 30)