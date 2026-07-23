#切片（slice）
lists = ['chen','dan','dan','chen','zhi','bin']
print(lists)

message = f"\nThe first three items is {lists[0:3]}"#在索引的第二个元素前停止
print(message)

message = f"\nThe middle three items is {lists[1:5]}"
print(message)

message = f"\nThe last three items is {lists[-3:]}"
print(message)
#元素之间记得用逗号隔开
#记得顺序数是从0开始数
#list（）是一个函数，避免占用