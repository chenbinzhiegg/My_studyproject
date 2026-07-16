person1={'first_name':'chen',
        'last_name':'zhibin',
        'age':19,
        'city':'nanan',
        }
person2={'first_name':'chen',
        'last_name':'eggegg',
        'age':19,
        'city':'quanzhou',
        }
person3={'first_name':'chen',
        'last_name':'binzhi',
        'age':19,
        'city':'fujian',
        }

peoples={'person1':person1,'person2':person2,'person3':person3}  #key不能变？

for people,info in peoples.items():
    print(f"{info['last_name']}")
    print(f"{info['city']}\n")