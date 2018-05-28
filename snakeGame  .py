#The snake game
from turtle import *
from random import randrange
from freegames import square,vector

# initialize food , which should be a square
food = vector(0,0)
# initialize the snake, which should be a list of squares
snake = [vector(10,0)]
# a snake's heading direction, which is a square
aim = vector(0,10)
#score
score = 0

# function that change snake's direction
def turn(x,y):
	aim.x = x
	aim.y = y

# function that check if the snake hits the canvas
def hitsTheWall(head):
	return -250 < head.x < 250 and -250 < head.y < 250

# function that moves the snake by one square
def moveOneSegment():
	#get a shallow copy of the head the snake
	#the last square of the snake is its head
	head = snake[-1].copy()
	#move the snake
	head.move(aim)

	#check if the snake hits the wall or snake bites itself
	if not hitsTheWall(head) or head in snake:
		#draw square
		square(head.x,head.y,9,'blue')
		update()
		return

	#move the head
	snake.append(head)

	#if it eats food, the snake grows
	if head == food:
		#randomlt generate new food
		food.x = randrange(-20,20) * 10
		food.y = randrange(-20,20) * 10
	#otherwise, get rid of the original square before snake moves
	#if it eats food we don't get rid of the original square as the snake grows
	else:
		snake.pop(0)

	#draw squares
	#draw snake
	clear()
	for body in snake:
		square(body.x,body.y,9,'black')

	#draw food
	square(food.x,food.y,9,'green')
	update()
	#delay 300ms
	ontimer(moveOneSegment,300)

#set up main canvas
def setUpGame():
	setup(500,500,450,0)
	hideturtle()
	tracer(False)
	listen()
	#keyboard control
	onkey(lambda: turn(10,0),'Right')
	onkey(lambda: turn(-10,0),'Left')
	onkey(lambda: turn(0,10),'Up')
	onkey(lambda: turn(0,-10),'Down')
	#start game
	moveOneSegment()
	done()

setUpGame()


