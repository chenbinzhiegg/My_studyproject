student = {"name": "Alice", "age": 20, "major": "Computer Science"}# 访问值
name = student["name"]  # "Alice"# 添加/修改元素
print(name)
student["grade"] = "A"      # 添加新键值对
student["age"] = 21         # 修改已有键的值方法
print(student)
keys = student.keys()       # 获取所有键
print(keys)
values = student.values()   # 获取所有值
print(values)
items = student.items()     # 获取所有键值对
print(items)