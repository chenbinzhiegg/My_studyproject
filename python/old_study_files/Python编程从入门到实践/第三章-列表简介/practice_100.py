list = ['xiaohong','xiaochen','xiaoming']
popped_list = []
print(list)
print(popped_list)

print("\n")
popped_element = list.pop(1)
print(list)
popped_list.append(popped_element)
print(popped_list)

print("\n")
popped_element = list.pop(1)
popped_list.append(popped_element)
print(list)
print(popped_list)

#popped_element 为字符串
#append() 方法为列表独有的，不能用于popped_element