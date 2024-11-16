import random, pgzrun
WIDTH=500
HEIGHT=500

alien=Actor("alien.png")
alien.pos=random.randint(0,500),random.randint(0,500)

message="click on the alien"

def draw():
    screen.fill("dark blue")
    alien.draw()
    screen.draw.text(message,center=(250,50),fontsize=30)
def coordinates():
    alien.x=random.randint(25,475)
    alien.y=random.randint(25,475)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        coordinates()
        message="well done"
    else:
        message="you missed"
clock.schedule_interval(coordinates,2)
pgzrun.go()