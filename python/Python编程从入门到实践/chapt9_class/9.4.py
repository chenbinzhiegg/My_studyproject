#餐馆

class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant=restaurant_name
        self.cuisine_type=cuisine_type
        
        self.number_served=0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is openning.")

    def set_number_served(self,numbers):
        self.number_served=numbers
    
    def increment_number_served(self,increment):
        self.number_served+=increment

my_restaurant=Restaurant('Egg','China')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(my_restaurant.number_served)

my_restaurant.set_number_served(1)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(1)
print(my_restaurant.number_served)