# TURTLE GRAPHICS
from turtle import Turtle, Screen

# jose = Turtle()
# jose.shape("turtle")#methods

jose = Turtle("turtle")
jose.color("DarkSeaGreen")
jose.shapesize(5)
jose.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #atribute
my_screen.exitonclick() #method

