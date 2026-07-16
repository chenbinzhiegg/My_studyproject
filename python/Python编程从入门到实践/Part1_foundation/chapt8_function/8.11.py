#消息归档


def send_messgaes(massages):
    """发送消息"""
    sent_massages=[]

    while massages:
        current_massage=massages.pop()
        print(current_massage)

        sent_massages.append(current_massage)
    
    return sent_massages

massages=['Hello','yes','I love you']

#sent_massages=send_messgaes(massages)
sent_massages=send_messgaes(massages[:])    #传递的是massages的副本，而massages不做改变

print(massages)
print(sent_massages)
