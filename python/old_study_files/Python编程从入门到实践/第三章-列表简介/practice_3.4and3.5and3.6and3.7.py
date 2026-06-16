list = ['xiaoming','xiaohong','xiaogang']
massage = f"I want to invite {list} to have a dinner ."
print(massage)

print("\n")
print(f"I'm sorry for hear that, {list[2].title()} can't  come.")
list[2] = 'xiaowang' #修改列表中的值
print(list)
massage = f"I want to invite {list} to have a dinner together."
print(massage)

print("\n")
print("Oh, I found a bigger table that can hold more people to come !")
list.insert(0,'xiaochen')#insert()在列表任意位置添加元素
list.insert(1,'xiaoli')
list.append('xiaohuang')#append()（追加） 将元素添加到末尾
massage = f"I want to invite {list} to have a dinner ."
print(massage)

print("\n")
print("Oh , no , there is somethong wrong . Now, I just can have dinner with two friends .")
popped_list = list.pop(1)#pop()（弹出）
print(f"Sorry , {popped_list} ,I can have dinner with you .")
popped_list = list.pop(1)
print(f"Sorry , {popped_list} ,I can have dinner with you .")
popped_list = list.pop(2)
print(f"Sorry , {popped_list} ,I can have dinner with you .")
popped_list = list.pop(2)
print(f"Sorry , {popped_list} , I can have dinner with you .")
print(list)
print(f"{list[1].title()} , I will have dinner with you . Only for you .")