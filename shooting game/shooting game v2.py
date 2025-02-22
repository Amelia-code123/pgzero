import pgzrun, random

WIDTH=800
HEIGHT=600

#variables
bullets=[]
score=0
speed=5
direction=1

ship=Actor("spaceship.png")
ship.pos=400,550
rows=[]

for i in range(6):
    rows.append(Actor("alien.png"))
    rows[-1].x=100+90*i
    rows[-1].y=0

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet.png"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y

def draw():
    screen.blit("background.jpg", (0,0))
    ship.draw()
    for e in rows:
        e.draw()
    screen.draw.text("Score:"+str(score),center=(50,50))
    for i in bullets:
        i.draw()

def update():
    global score, direction
    movedown=False
    pass
    if keyboard.left:
        ship.x-=speed
    if keyboard.right:
        ship.x+=speed
    if len(rows)>0 and (rows[-1].x>WIDTH-80 or rows[0].x<80):
        movedown=True
        direction=direction*-1
    for e in rows:
        e.x +=5*direction
        if movedown==True:
            e.y+=25
        for i in bullets:
            i.y-=8
            if i.colliderect(e):
                e.x=random.randint(0,800)
                e.y=50
                bullets.remove(i)
                rows.remove(e)
                sounds.eep.play()
                score=score+1

pgzrun.go()