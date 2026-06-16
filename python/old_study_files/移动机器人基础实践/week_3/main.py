import PersonClass as Ps

my_mom = Ps.Person('Alice',30,'female')
my_son = Ps.Professor('Eric',20,'male','Peking University')
my_father = Ps.Engineer('Jack',31,'male','HUAWEI')

my_mom.introduce()
print("\n")

my_son.introduce()
my_son.school()
print("\n")

my_father.introduce()
my_father.workplace()
print("\n")


#更新年龄
my_mom.update_age(input("请更新Alice的年龄："))
