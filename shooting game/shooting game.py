import pgzrun, random

WIDTH=800
HEIGHT=600

#variables
bullets=[]
score=0
speed=5

ship=Actor("spaceship.png")
alien=Actor("alien.png")
ship.pos=400,550
alien.x=random.randint(0,800)
alien.y=50

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet.png"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y

def draw():
    screen.blit("background.jpg", (0,0))
    ship.draw()
    alien.draw()
    for i in bullets:
        i.draw()

def update():
    pass
    if keyboard.left:
        ship.x-=speed
    if keyboard.right:
        ship.x+=speed
    for i in bullets:
        i.y-=8
        if i.colliderect(alien):
            alien.x=random.randint(0,800)
            alien.y=50
            bullets.remove(i)
            sounds.eep.play()

pgzrun.go()