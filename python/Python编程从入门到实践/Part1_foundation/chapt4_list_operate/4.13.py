#元组：不可变的 用()来表示
types = ('ji','ya','yu','dan','nai')
print("Original types is :")
for type in types :
    print(type)

#types[0] = 'niu'
#无法尝试修改列表中的值

#重新定义整个元组
types = ('niu','yang','yu','dan','nai')
print("\nNew types is :")
for type in types :
    print(type)

