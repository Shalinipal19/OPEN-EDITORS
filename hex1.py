from turtle import *
#hexagon
speed('fastest')
pencolor('blue')
pensize(2)
for i in range(90):
    fd(100-i)
    rt(60)
    circle(100,270)
    dot(25,'yellow')
mainloop()    