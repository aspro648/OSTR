# https://runestone.academy/ns/books/published/pythonds/Recursion/pythondsSierpinskiTriangle.html

from turtle import *

def drawTriangle(points):
    penup()
    goto(points[0][0],points[0][1])
    pendown()
    goto(points[1][0],points[1][1])
    goto(points[2][0],points[2][1])
    goto(points[0][0],points[0][1])


def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree=2):
    drawTriangle(points)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]),
                    getMid(points[0], points[2])], degree-1)
        sierpinski([points[1], getMid(points[0], points[1]),
                    getMid(points[1], points[2])], degree-1)
        sierpinski([points[2], getMid(points[2], points[1]),
                    getMid(points[0], points[2])], degree-1)


myPoints = [[-75,-50],[0,50],[75,-50]]
sierpinski(myPoints, degree = 2)
penup()
forward(100)
