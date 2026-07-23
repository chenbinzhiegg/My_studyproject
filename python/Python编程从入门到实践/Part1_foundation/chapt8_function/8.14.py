#汽车

def make_car(manufacturer,types,**more):
    more['manufacturer']=manufacturer
    more['type']=types
    
    return more

car = make_car('subare','outback',color='blue',tow_package=True)
print(car)