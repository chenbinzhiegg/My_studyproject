#餐馆

class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant():
        print("The restaurant is openning.")

my_restaurant=Restaurant('Egg','China')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant