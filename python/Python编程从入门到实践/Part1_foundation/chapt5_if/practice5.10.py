current_users = ["huang","la","lin",'chen','zhi','bin']
new_users = ["huang","Hong",'chen']

for user in new_users :
    if user.lower() in current_users :
        print(f"You can't use {user} as your name .")
    else :
        print(f"You can use {user} as your name .")