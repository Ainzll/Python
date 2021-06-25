#MODULE 7 - Pythin Turtle graphics
#https://docs.python.org/3/library/turtle.html (Links to an external site.)
#Before using turtle install turtle graphics.
#sudo apt install python3-tk python-tk
#
#Try this code:

import turtle
from random import randrange
w = turtle.Screen()
w.clear()
w.bgcolor("#ffffff")
t = turtle.Turtle()
t2 = turtle.Turtle()
#turtle.tracer(0, 0)
# - - - - -
n = 0
colors = ['#ff0000','#ffff00','#00ff00','#00ffff','#0000ff','#ff00ff']
a=1
siz = randrange(10,50)
pencol = colors[randrange(0,6)]
t.speed('fastest')
t2.speed('fastest')
crdX = randrange(-500,500)
crdX2 = randrange(-500,500)
crdY = randrange(-500,500)
crdY2 = randrange(-350,350)
while a==1:
	def petal1(angle,length,coordx,coordy):
		t.penup()
		t.pencolor(pencol)
		t.goto(coordx,coordy)
		t.pendown()
		t.right(angle)
		t.forward(length)
		t.right(angle + 17)
		t.forward(length)
		t.right(17)
		t.forward(length)
		t.goto(coordx,coordy)
		
	def petal2(angle,length,coordx2,coordy2):
		t2.penup()
		t2.pencolor(pencol)
		t2.goto(coordx2,coordy2)
		t2.pendown()
		t2.right(angle)
		t2.forward(length)
		t2.right(angle + 17)
		t2.forward(length)
		t2.right(17)
		t2.forward(length)
		t2.goto(coordx2,coordy2)
	
	petal1(0,siz,crdX,crdY)
	petal2(0,siz,crdX2,crdY2)
	n += 1
	if n % 1 == 0:
		
		pencol = colors[randrange(0,6)]
	if n == 21:
		n = 0
		siz = randrange(10,50)
		crdX = randrange(-800,800)
		crdX2 = randrange(-800,800)
		crdY = randrange(-350,350)
		crdY2 = randrange(-350,350)
#turtle.update()
w.exitonclick()
