my_pizzas = ['niurou','tianyuan','liulian']
friend_pizzas = my_pizzas[:]
#两变量刚好相同，复制一个副本给新的变量
#[:]同时省略起始索引和终止索引
my_pizzas.append('caomei')
friend_pizzas.append("qiaokeli")

print("My favorite pizzas are:")
for pizza in my_pizzas :
    print(pizza)

print("\nMy friend favorite pizzas are:")
for pizza in friend_pizzas :
    print(pizza)