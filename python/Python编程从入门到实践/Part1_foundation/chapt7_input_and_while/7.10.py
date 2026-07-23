#度假地询问

responses={}
active=True

while active:   #falg
    name=input("What is your name ? ")
    response=input("If you could visit one place in the world , where would you go ?")

    responses[name]=response

    repeat=input("Would you like to let another person respond ? (yes/no)")
    if repeat == 'no' : #判断是否终止
        active =False

for name,response in responses.items(): #要用.items()返回键值对
    print(f"{name} like to the {response}.")



