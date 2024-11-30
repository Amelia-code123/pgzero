import pgzrun, random
WIDTH=700
HEIGHT=640

octopus=Actor("octopus.png")
fish=Actor("small fish.png")

def draw():
    screen.blit("underwater background",(0,0))
    octopus.draw()
    fish.draw()

def update():
    pass

pgzrun.go()