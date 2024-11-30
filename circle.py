import pgzrun, random
WIDTH=500
HEIGHT=500

def draw():
    r=200
    for i in range(30):
        red=random.randint(0,255)
        blue=random.randint(0,255)
        green=random.randint(0,255)
        screen.draw.circle((250,250),r,(red, green, blue))
        r-=5

def update():
    pass

pgzrun.go()