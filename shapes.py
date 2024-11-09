import pgzrun, random

WIDTH=300
HEIGHT=300

def draw():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    width=300
    height=150
    for i in range(20):
        rect=Rect((0,0),(width,height))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))
        width-=10
        height+=10

pgzrun.go()