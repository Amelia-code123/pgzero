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
questionbox=Rect(25,100,625,100)
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
    screen.draw.filled_rect(questionbox,"pink")
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
    screen.draw.textbox(question[0].strip(),questionbox,color="black")
    ind=1
    for i in boxes:
        screen.draw.textbox(question[ind].strip(),i,color="black")
        ind=ind+1

#function for correct answer
def correct():
    global score, question, timerr, questions
    score=score+1
    if questions:
        question=nextq()
        timerr=15
    else:
        game_over()

def on_mouse_down(pos):
    ind=1
    for i in boxes:
        if i.collidepoint(pos):
            if ind is int(question[5]):
                correct()
            else:
                game_over()
        ind=ind+1
    if skip.collidepoint(pos):
        skipf()

#skip function
def skipf():
    global question, timerr
    if questions and not gameover:
        question=nextq()
        timerr=15
    else:
        game_over()

#game over function
def game_over():
    global gameover, score, question, timerr
    message=f"Game Over! \n You got {score} questions correct!"
    question=[message,"-","-","-","-",5]
    timerr=0
    gameover=True

#reading the question file
def readq():
    global questions, count
    file=open("questions.txt", "r")
    for i in file:
        questions.append(i)
        count=count+1
    file.close()

#reading next question every time
def nextq():
    global index
    index=index+1
    return questions.pop(0).split(",")

#marquee function
def move():
    marquee.x-=3
    if marquee.right<0:
        marquee.left=800

def updatetime():
    global timerr
    if timerr>0:
        timerr=timerr-1
    else:
        game_over()

def update():
    pass
    move()

readq()
question=nextq()

clock.schedule_interval(updatetime, 1)

pgzrun.go()
