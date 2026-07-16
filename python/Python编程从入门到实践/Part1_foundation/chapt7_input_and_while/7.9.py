#熟食店制作
#五香烟熏牛肉卖完了

sandwich_orders=['zhurou','niurou','shucai','pastrami','pastrami','pastrami']
finished_sandwiches=[]

print("The pastrami had sell out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders :
    current_sandwich=sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich !")

    finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)



