import pgzrun, random, time

WIDTH=800
HEIGHT=600

start=0
end=0
all=[]
lines=[]
next=0

def flowers():
    global start
    for i in range(10):
        flower=Actor("flower.png")
        flower.pos=random.randint(50, 750),random.randint(50, 550)
        all.append(flower)
    start=time.time()

def draw():
    screen.blit("grass.jpg", (0,0))
    count=1
    for i in all:
        i.draw()
        screen.draw.text(str(count),(i.pos[0],i.pos[1]))
        count=count+1
    for x in lines:
        screen.draw.line(x[0],x[1],"pink",width=5)

def update():
    pass

def on_mouse_down(pos):
    global next, lines
    if next < 10:
        if all[next].collidepoint(pos):
            if next:
                lines.append((all[next-1].pos, all[next].pos))
            next=next+1
flowers()

pgzrun.go()
