#抛硬币

import random

times=0
time1=0
time2=0

times=int(input("请输入抛硬币的次数："))    #input默认是str类型，要做类型转换
possible = [0,1]

for i in range(1,times+1):
    tempo=random.choice(possible)
    if(tempo==0):
        time1+=1
    else:
        time2+=1

t=time2/times

print(f"抛{times}次，硬币朝上的概率是：{t*100:.2f}%")


