class Cat:
    def __init__(self,cat_name,cat_age):
        self.name = cat_name
        self.age = cat_age
    
    def run(self):
        print(f"{self.name} is running.")

    def sit(self):
        print(f"{self.name} is sitting.")

my_cat = Cat('kity',100)
my_cat.name = 'aaaa'
your_cat = Cat('Jack',4)
his_cat = Cat('Lubby',3)
my_cat.run()
my_cat.sit()
print(f"{my_cat.name} is {my_cat.age} years old.")