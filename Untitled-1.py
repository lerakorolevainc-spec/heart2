import math
from turtle import *
def h(k):
    return 15*math.sin(k)**3
def e(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
speed(500000)
bgcolor('black')
for i in range(6000):
    goto(h(i)*20,e(i)*20)
    color("#300098")
done()
