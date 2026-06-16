users_lists = ['chen','egg','egg','chen','zhi','bin']
if users_lists :    #检查列表是否为空
    for user in users_lists :
        if user == "egg" :
            print("Hello ,egg, would like to go with me ?")
        else :
            print(f"Hello ,{user} .")
else :
    print("I need you .")