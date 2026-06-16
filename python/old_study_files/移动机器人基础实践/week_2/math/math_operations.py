def add(a,b):
    add_result = a+b
    return add_result

def subtract(a,b):
    subtract_result = a-b
    return subtract_result

def multiply(a,b):
    multiply_result = a*b
    return multiply_result

def divide(a,b):
    if b == 0 :
        divide_result = "除数不能为0"
    else:   
        divide_result = a/b
    return divide_result

def power(a,b):
    power_result = a**b
    return power_result

def factorial(n):
    i=1
    r=1
    while i<=n :
        r = r*i
        i=i+1       
    factorial_result = r  
    return factorial_result
    