import pgzrun, random
WIDTH=700
HEIGHT=640

octopus=Actor("octopus.png")
fish=Actor("small fish.png")
fish.pos=(350,320)

def draw():
    screen.blit("underwater background",(0,0))
    octopus.draw()
    fish.draw()

def update():
    pass
    if keyboard.left:
        octopus.x-=5
    if keyboard.right:
        octopus.x+=5
    if keyboard.up:
        octopus.y-=5
    if keyboard.down:
        octopus.y+=5
    if octopus.colliderect(fish):
        coordinates()

def coordinates():
    fish.x=random.randint(50,650)
    fish.y=random.randint(50,600)

pgzrun.go()
