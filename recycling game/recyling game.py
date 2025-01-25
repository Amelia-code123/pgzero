import pgzrun, random

WIDTH=800
HEIGHT=600

levels=6
speed=3
notrecyclable=["battery.png","crisp packet.png", "plastic bottle.png"]
end=False
current=1
items=[]

def draw():
    screen.blit("background.jpg", (0,0))

def update():
    pass

def order(extra):
    empty=[]
    options=["paper bag.jpg"]+random.choices(notrecyclable,k=extra)
    random.shuffle(options)
    for i in options:
        item=Actor(i)
        empty.append(item)
    gap=WIDTH/len(empty)+1
    for index,item in enumerate(empty):
        item.x=(index+1)*gap
        item.y=0
        animate(item,duration=speed-current,on_finished=gameover,y=HEIGHT)

pgzrun.go()