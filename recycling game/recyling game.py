import pgzrun, random

WIDTH=800
HEIGHT=600

levels=6
speed=10
notrecyclable=["battery.png","crisp packet.png", "plastic bottle.png"]
end=False
current=1
items=[]
win=False

def draw():
    screen.blit("background.jpg", (0,0))
    if end==True:
        screen.draw.text("Game Over",center=(400,100),fontsize=50,color="red")
    elif win==True:
        screen.draw.text("You Win! Well Done!",center=(400,100),fontsize=50,color="blue")
    else:
        for i in items:
            i.draw()

def update():
    pass
    global items, current
    if len(items)==0:
        items=order(current)

def order(extra):
    empty=[]
    options=["paper bag.png"]+random.choices(notrecyclable,k=extra)
    random.shuffle(options)
    for i in options:
        item=Actor(i)
        empty.append(item)
    gap=WIDTH/(len(empty)+1)
    for index,item in enumerate(empty):
        item.x=(index+1)*gap
        item.y=0
        animate(item,duration=speed-current,on_finished=gameover,y=HEIGHT)
    return empty

def gameover():
    global end
    end=True

def on_mouse_down(pos):
    global items, current, win
    for i in items:
        if i.collidepoint(pos):
            if "paper bag" in i.image:
                if current==levels:
                    win=True
                else:
                    current=current+1
                    items.clear()
            else:
                gameover()

pgzrun.go()
