#城市

def describe_city(city,country='china'):
    """打印一个城市在一个国家"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('quanzhou')
describe_city(city='xiamen')
describe_city(city='New York',country='US')