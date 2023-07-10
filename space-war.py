import random
import turtle
import winsound

window=turtle.Screen()
window.bgcolor("black")
window.title("Space War")
window.bgpic("space.gif")
window.setup(width=600, height=600)

turtle.register_shape('player.gif')
turtle.register_shape('enemy.gif')
turtle.register_shape('fire.gif')

player=turtle.Turtle()
player.color('blue')
player.speed(0)
player.shape('player.gif')
player.setheading(90)
player.penup()
player.goto(0, -250)
playerSpeed=20

fire=turtle.Turtle()
fire.color('yellow')
fire.speed(0)
fire.shape('fire.gif')
fire.setheading(90)
fire.penup()
fire.goto(0, -240)
fireSpeed=20
fire.hideturtle()
fire.turtlesize(1,1)
firecontrol=False

write=turtle.Turtle()
write.color('white')
write.speed(0)
write.penup()
write.goto(0,200)
write.hideturtle()

enemys=[]
for i in range(7):
    enemys.append(turtle.Turtle())
for enemy in enemys:   
    enemy.color('red')
    enemy.speed(0)
    enemy.turtlesize(1,1)
    enemy.shape('enemy.gif')
    enemy.penup()
    enemy.setheading(90)
    x=random.randint(-280,280)
    y=random.randint(180,260)
    enemy.goto(x,y)


def gofire():
    y=fire.ycor()
    y=y+fireSpeed
    fire.sety(y)

def go_left():
    x=player.xcor()
    x=x-playerSpeed
    if x<-300:
        x=-300
    player.setx(x)

def go_right():
    x=player.xcor()
    x=x+playerSpeed
    if x>300:
        x=300
    player.setx(x)    

def go_up():
    y=player.ycor()
    y=y+playerSpeed
    if y> 270:
        y=270
    player.sety(y)

def go_down():
    y=player.ycor()
    y=y-playerSpeed
    if y< -270:
        y=-270
    player.sety(y)

def shoot():
    global firecontrol
    winsound.PlaySound('laser.wav',winsound.SND_ASYNC)
    x=player.xcor()
    y=player.ycor()
    fire.goto(x,y)
    fire.showturtle()
    firecontrol=True



window.listen()
window.onkey(go_left,'Left')
window.onkey(go_right,'Right')
window.onkey(go_up,'Up')
window.onkey(go_down,'Down')
window.onkey(shoot,'space')


while True:
    if firecontrol:
        gofire()
    for enemy in enemys:
        y=enemy.ycor()
        y=y-2
        enemy.sety(y)
        if enemy.distance(fire)<20:
            winsound.PlaySound('boom.wav',winsound.SND_ASYNC)
            fire.hideturtle()
            enemy.hideturtle()
            enemys.pop(enemys.index(enemy))

        if enemy.ycor()<-270 or enemy.distance(player)<20:
             write.write('You Lost', align='center',font=18)    
             turtle.done()    

    if len(enemys)==0:
        write.write('Congratulations, you won!', align='center',font=18)       
        turtle.done() 



