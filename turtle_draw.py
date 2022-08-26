'''
import turtle

turtle.shape('turtle')
turtle.turtlesize(3)
turtle.pensize(3)
turtle.pencolor("red")


turtle.forward(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
'''
#202207000 김혜숙_1주
#집모양 그리기

import turtle
print('실행 결과')
t=turtle.Turtle()
t.shape('turtle')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100) # 사각형

t.right(30)
t.forward(100) 
t.right(120)
t.forward(100) 
