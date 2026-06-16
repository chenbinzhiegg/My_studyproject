#实现1-10的立方数列表

numbers = []
for number in range(1,11):
    squares = number**3
    numbers.append(squares)
print(numbers)