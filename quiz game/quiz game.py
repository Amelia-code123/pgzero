import pgzrun

WIDTH=800
HEIGHT=600

#variables
score=0
timerr=15
message="Welcome to Quiz Game!"
gameover=False

#boxes for the quiz
marquee=Rect(0,0,800,75)
question=Rect(25,100,625,100)
answer1=Rect(25,250,300,150)
answer2=Rect(350,250,300,150)
answer3=Rect(25,425,300,150)
answer4=Rect(350,425,300,150)
timer=Rect(680,100,100,100)
skip=Rect(680,250,100,325)
boxes=[answer1,answer2,answer3,answer4]
questions=[]
count=0
index=0

def draw():
    screen.draw.filled_rect(marquee,"black")
    screen.draw.filled_rect(question,"pink")
    screen.draw.filled_rect(answer1,"light blue")
    screen.draw.filled_rect(answer2,"light blue")
    screen.draw.filled_rect(answer3,"light blue")
    screen.draw.filled_rect(answer4,"light blue")
    screen.draw.filled_rect(timer,"pink")
    screen.draw.filled_rect(skip,"pink")
    #text boxes
    screen.draw.textbox(message, marquee, color="white")
    screen.draw.textbox(str(timerr), timer, color="black")
    screen.draw.textbox("SKIP", skip, color="black", angle=-90)

#marquee function
def move():
    marquee.x-=3
    if marquee.right<0:
        marquee.left=800

def updatetime():
    global timerr
    if timerr>0:
        timerr=timerr-1

def update():
    pass
    move()

clock.schedule_interval(updatetime, 1)

pgzrun.go()
