import pgzrun, random, time

WIDTH=800
HEIGHT=800

start=0
end=0
all=[]

def flowers():
    global start
    for i in range(10):
        flower=Actor("flower.png")
        flower.pos=random.randint(50, 750),random.randint(50, 750)
        all.append(flower)
    start=time.time()

def draw():
    screen.blit("grass.jpg", (0,0))
    for i in all:
        i.draw()

def update():
    pass

flowers()

pgzrun.go()
