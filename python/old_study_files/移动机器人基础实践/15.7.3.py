class Car:
    def __init__(self,T_maker,T_model,T_year):
        self.maker=T_maker
        self.model=T_model
        self.year=T_year
        #默认汽车的里程表读数是0
        self.odometer_reading=0

    def get_description(self):
        print(f"{self.year} {self.maker} {self.model}")

    def undate_odometer(self,mileage):
        self.odometer_reading=mileage

    def increment_odometer(self,miles):
        self.odometer_reading=self.odometer_reading+miles
    def get_odometer(self):
        print(f"汽车当前里程是{self.odometer_reading}公里")

class ElectricCar(Car):
    def __init__(self,T_maker,T_model,T_year,T_price):
        super().__init__(T_maker,T_model,T_year)
        self.battery_miles=550
        self.price=T_price
        self.color="green"

    def get_ELdescription(self):
        print(f"汽车年份:{self.year},制造商:{self.maker}，型号:{self.model}，价格:{self.price}万元,里程表读数：{self.odometer_reading}公里")
my_newcar=ElectricCar("Li","L9",2023,30)
my_newcar.get_ELdescription()