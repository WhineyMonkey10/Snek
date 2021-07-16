import turtle
import random

screen = turtle.Screen()  # creates the screen
screen.bgcolor('white')  # sets background as white
sprite = turtle.Turtle()  # defines the variable sprite as a turtle
sprite.shape('square')
sprite.penup()
sprite.speed(0)
sprite.goto(-500, 500)
sprite.speed(0)
screen.addshape("head.gif")
screen.addshape("tren.gif")
screen.addshape("body.gif")
game_over = sprite.clone()
# sprite.shapesize(1)

snek = []
food = None


def create_food():
    global food
    food = sprite.clone()
    food.color('red')
    food.shape("tren.gif")

    random_x = random.randint(-8, 8) * 44  # Generating random x coord for apple
    random_y = random.randint(-8, 8) * 44  # Generating random x coord for apple
    food.goto(random_x, random_y)


running = True  # to keep track of weather the game is running


def create_body(x, y):
    body = sprite.clone()  # create the body
    body.color('green')  # makes the snek green
    body.shape("head.gif")
    body.goto(x, y)  # moving the body

    body.speed(0)
    snek.append(body)  # adding the body to the snake (so it can get bigger)


direction = 0


def move():
    global running
    tail = snek[len(snek) - 1]  # get the tail of the snake
    head = snek[0]  # get the head of the snake
    x = head.xcor()  # get the x coordinate of the snake head
    y = head.ycor()  # get the y coordinate of the snake head
    size = 44  # size of square is 44 px

    if direction == 'down':
        tail.goto(x, y - size)  # tail goes 22 pixels down
        tail.shape("head.gif")
    elif direction == 'up':
        tail.goto(x, y + size)  # tail goes 22 pixels up
        tail.shape("head.gif")
    elif direction == 'right':
        tail.goto(x + size, y)  # tail goes 22 pixels right
        tail.shape("head.gif")
    elif direction == 'left':
        tail.goto(x - size, y)  # tail goes 22 pixels left
        tail.shape("head.gif")
    for i in range(len(snek) - 1):
        snek[i].shape("body.gif")

    for i in range(1, len(snek)):
        if x == snek[i].xcor() and y == snek[i].ycor():
            running = False

    if x >= (screen.screensize()[0] - 2 * size) or x <= (- screen.screensize()[0] + 2 * size):
        x = -x
        running = False
    if y >= (screen.screensize()[1] + size) or y <= (- screen.screensize()[1] - size):
        y = -y
        running = False


    snek.insert(0, tail)  # move tail to the head
    snek.pop()  # Remove the last element of the list


def up():
    global direction
    if not direction == 'down':
        direction = 'up'


def down():
    global direction
    if not direction == 'up':
        direction = 'down'


def right():
    global direction
    if not direction == 'left':
        direction = 'right'


def left():
    global direction
    if not direction == 'right':
        direction = 'left'


screen.onkey(up, "w")
screen.onkey(left, "a")
screen.onkey(down, "s")
screen.onkey(right, "d")

screen.onkey(up, "Up")
screen.onkey(left, "Left")
screen.onkey(down, "Down")
screen.onkey(right, "Right")
screen.listen()


def update():
    if running:
        move()  # Move the snake at every screen refresh
        head = snek[0]
        x = head.xcor()
        y = head.ycor()
        if x == food.xcor() and y == food.ycor():
            create_body(x, y)
            food.hideturtle()
            create_food()
        screen.ontimer(update, 250)  # Set how fast it's updating the screen
    else:
        game_over.clear()
        game_over.hideturtle()
        game_over.goto(10, 10)
        game_over.write("Game over. Press R to restart", align="center", font=("Arial", 24, "bold"))
        screen.onkey(restart, "r")



def restart():
    global running
    global snek
    snek = []
    running = True
    screen.clearscreen()
    start_game()


def start_game():
    global running
    running = True
    sprite.speed(0)
    create_body(0, 0)
    create_food()  # creates food in random location
    update()


start_game()

turtle.done()  # tells it when it's done

# todo: create boundry

