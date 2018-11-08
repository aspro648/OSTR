from turtle import *

arms = 1
length = 50

#setDebug(True)

pendown()

for i in range(arms):
  forward(length)
  '''
  left(45)
  forward(length / 2)
  backward(length / 2)
  right(90)
  forward(length / 2)
  backward(length / 2)
  left(45)
  '''
  backward(length)
  right(360/arms)
forward(length)
  
penup()
done()
