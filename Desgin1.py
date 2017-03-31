from MyFunction import *
import turtle
bob=turtle.Turtle()
wavy=turtle.Turtle()
lit=turtle.Turtle()
coolio=turtle.Turtle()
ma=turtle.Turtle()
sun=turtle.Turtle()
moon=turtle.Turtle()


#changes_background_color
turtle.bgcolor("black")


#controls_speed
bob.speed(0)
wavy.speed(0)
lit.speed(0)
coolio.speed(0)
ma.speed(0)
sun.speed(0)
moon.speed(0)


turtle.colormode(255)


wavy.left(180)
lit.left(90)
coolio.left(270)


#Creates_sprialing_star
for times in range(125):
	ma.width(3)
	ma.color(255,50+times,0)
	star(ma,100+times)
	ma.left(275)


#creates_sprialing_square
for times in range(100):
	bob.width(3)
	c=(56,255-times,96)
	bob.color(255,100+times,0)
	print(c)
	polygon(bob,4,times*2)
	bob.left(275)


	wavy.width(3)
	wavy.color(255,100+times,0)
	polygon(wavy,4,times*2)
	wavy.left(275)


	lit.width(3)
	lit.color(255,100+times,0)
	polygon(lit,4,times*2)
	lit.left(275)


	coolio.width(3)
	coolio.color(255,100+times,0)
	polygon(coolio,4,times*2)
	coolio.left(275)


#creates_outlined_star
for times in range(100):
	sun.width(0)
	sun.begin_fill()
	sun.color(255,50+times,100-times)
	moon.color(255,50,100+times)
	star(sun,100-times)
	star(moon,100-times)
	moon.left(275)
	sun.left(275)
	sun.end_fill()







