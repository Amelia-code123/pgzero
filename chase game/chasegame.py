import pgzrun, random
WIDTH=700
HEIGHT=640

octopus=Actor("octopus.png")
fish=Actor("small fish.png")
fish.pos=(350,320)
score=0
gameover=False

def draw():
    screen.blit("underwater background",(0,0))
    octopus.draw()
    fish.draw()
    screen.draw.text(str(score),topright=(650,50),fontsize=60)
    if gameover==True:
        screen.fill("light blue")
        screen.draw.text("Time is up!",center=(350,320),fontsize=70)
        screen.draw.text("Score="+str(score),center=(350,390),fontsize=60)

def update():
    global score
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
        score+=1

def over():
    global gameover
    gameover=True

def coordinates():
    fish.x=random.randint(50,650)
    fish.y=random.randint(50,600)

clock.schedule(over,60)

pgzrun.go()
