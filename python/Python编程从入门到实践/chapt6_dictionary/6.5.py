#河流
rivers={'changjiang':'China','nile':'Egypt'}

for key,value in rivers.items():    #.items:返还一个键值对列表
    print(f"The {key} runs thrhoug {value}") 

for key in rivers.keys():
    print(f"{key}")

for value in rivers.values():
    print(f"{value}")

names=['changjiang','huanghe']
for river in names:
    if river  in rivers:
        print(f"The {river}  in the lists.")
    else :
        print(f"The {river}  not in then lists.")