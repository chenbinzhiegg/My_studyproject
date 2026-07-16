#冰淇淋小店

#餐馆

class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant=restaurant_name
        self.cuisine_type=cuisine_type
        
        self.number_served=0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant}")
        print(f"The cuisine type is {self.cuisine_type}")


class IceCreamStand(Restaurant):    #要标明父类
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)  # 用super() 调用父类的方法
        self.flavor=[]  #子类特有的属性
    
    def describe_restaurant(self):
        super().describe_restaurant()

    def show_flavor(self):
        print(self.flavor)

my_restaurant=IceCreamStand('Egg','China')

my_restaurant.describe_restaurant()

my_restaurant.flavor.append('1')
my_restaurant.show_flavor()


