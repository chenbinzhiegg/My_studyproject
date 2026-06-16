import turtle
t = turtle.Turtle()
t.speed(2)

#绘制黄色建筑主体
t.color("green")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup
t.forward(100)
t.left(90)
t.forward(100)

#绘制红色屋顶
t.color("red")
t.begin_fill()
t.left(45)
t.forward(70)
t.left(90)
t.forward(70)
t.end_fill()

#回到起点
t.hideturtle()  # 隐藏海龟光标
turtle.done()