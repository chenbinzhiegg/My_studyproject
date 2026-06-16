class Person:  #定义一个名为Person的父类
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello,my name is {self.name} , I am {self.age} old ,and I am {self.gender}  .")
    
#更新年龄
    def update_age(self,new_age):
        while True:
            try:
                new_age = float(new_age)
                new_age =  int(new_age)
                self.age = new_age
                print(f"{self.name}的年龄已更新为:{self.age}")
                break
            except:
                print("输入的年龄格式有误")
                new_age = input("请再次输入年龄：")
                continue
                    
        

#子类
class Professor(Person):  #定义一个名为Professor的子类
    def __init__(self,name,age,gender,university):
        super().__init__(name,age,gender)
        self.university = university
    
    def school(self):
        print(f"I am working in the {self.university} .")


class Engineer(Person):  #定义一个名为Engineer的子类
    def __init__(self,name,age,gender,compony):
        super().__init__(name,age,gender)
        self.compony = compony

    def workplace(self):
        print(f"I am working in the {self.compony} .")
        
        