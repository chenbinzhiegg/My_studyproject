# 1. 创建学生和成绩列表
students = ["小明", "小红", "小刚"]
scores = [[80, 85], [90, 95], [70, 75]]  # 每个学生两门课成绩

print("学生:", students)
print("成绩:", scores)
print()

# 2. 添加新学生
students.append("小丽")
scores.append([88, 92])
print("添加小丽后:")
print("学生:", students)
print("成绩:", scores)
print()

# 3. 修改成绩
# 修改小红的数学成绩（第2门课）
scores[1][1] = 100
print("修改小红数学成绩为100:")
print("小红成绩:", scores[1])
print()

# 4. 计算每个学生平均分
for i in range(len(students)):
    avg = (scores[i][0] + scores[i][1]) / 2
    print(f"{students[i]}平均分: {avg}")
print()

# 5. 查找全班最高分
all_scores = []
for s in scores:
    all_scores.extend(s)

print("所有成绩:", all_scores)
print("最高分:", max(all_scores))
print("最低分:", min(all_scores))

# 6. 按平均分排序
# 先计算平均分
averages = []
for s in scores:
    averages.append((s[0] + s[1]) / 2)

# 组合排序
sorted_list = sorted(zip(averages, students), reverse=True)  #zip(a,b)把两个列表按位置配对成元组
print("\n成绩排名:")
for i, (avg, name) in enumerate(sorted_list, 1):  #enumberate(列表，1)生成从1开始的序号
    print(f"第{i}名: {name} ({avg:.1f}分)")  #{avg:1f}  把平均分保留一位小数输出