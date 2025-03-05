import pgzrun
from random import randint


# music
music.play_once("cat")
music.queue("dog")
music.queue("h")

# game HEIGHT and WIDTH
WIDTH = 1247
HEIGHT = 700
# player
alien = Actor("pl")
alien.gravity = 0
alien.points = 0
alien.gameover = False
alien.started = False
alien.level = 1

#dim
dim = Actor("dim")
dim.right = WIDTH
dim.bottom = HEIGHT
#power
arm = Actor("fre")
arm1 = Actor("arm")

# blocks and enimes
mine = Actor("mine")
mine.right = WIDTH
mine.bottom = HEIGHT
mine2 = Actor("mine2")
mine2.x = randint(0, WIDTH)
mine2.y = 0
#mine3 = Actor("mine3")
pigm = Actor("pigmen")
pigm.right = WIDTH
pigm.bottom = HEIGHT
zom = Actor("zom")
zom.right = WIDTH
zom.bottom = HEIGHT
cat = Actor("asf")
cat.right = WIDTH
cat.bottom = HEIGHT
bg = Actor("back")


def draw():
    bg.draw()  # background level 1
    screen.draw.text(f"Points: {alien.points}", (10, 10), color="black")  # points and level
    screen.draw.text(f"level: {alien.level}", (10, 40), color="black")
    alien.draw()  # player
    arm.draw()
    arm1.draw()
    dim.draw()
    mine.draw()#mine1
    mine2.draw()#mine2
    #mine3.draw()#mine3
    zom.draw()# zombie
    pigm.draw()# pigmen
    cat.draw() # catus

    # gameover screen
    if alien.gameover:
        screen.fill("red")
        screen.draw.text("GAME OVER", (200, 200))


def update():

    if dim.colliderect(alien):
        alien.points += 1
        dim.x += 7
    # points level 2  background 2
    if alien.points > 200:
        bg.image = "gre"
        zom.x -= 7
        if zom.colliderect(alien):
            alien.gameover = True
            #arm defeander
        if zom.colliderect(arm):
            zom.right = 2000
            alien.points += 1
            #level
        alien.level = 2

    # points level 3  background 3
    if alien.points > 600:
        bg.image = "rfd"
        pigm.x -= 7
        if pigm.colliderect(alien):
            alien.gameover = True
        if pigm.colliderect(arm):
            pigm.right = 3000
            alien.points += 5
        alien.level = 3
    # points level 4  background 4
    if alien.points > 1000:
        bg.image = "aw"
        mine.x -= 7
        if mine.colliderect(alien):
            alien.gameover = True
        if mine.colliderect(arm):
            mine.right = 4000
            alien.points = 10
        alien.level = 4
    if alien.points > 3000:
        mine2.x -= 7
        if mine2.colliderect(alien):
            alien.gameover = True
        if mine2.colliderect(arm1):
            mine2.y = 0
            mine2.x = randint(0, WIDTH)
            alien.points = 50
    #if alien.points > 4000:
    if alien.points > 5000:
        bg.image = "you win"

    arm.x += 20
    arm1.y -= 20
    dim.x += 20
    # movement
    alien.gravity += 1
    alien.y += alien.gravity
    if alien.bottom >= HEIGHT:
        alien.bottom = HEIGHT
        alien.gravity = 0
    if keyboard.up and alien.bottom == HEIGHT:
        alien.gravity = -30
        alien.started = True
        sounds.l.play()
        if alien.points < 10:
            alien.points += 10
        elif alien.points < 11:
            alien.points += 5
        else:
            alien.points += 1
    if keyboard.left:
        alien.x -= 5
        alien.started = True
    if keyboard.right:
        alien.x += 5
        alien.started = True
    if keyboard.a:
        arm.pos = alien.pos
        alien.started = True
    if keyboard.s:
        arm1.pos = alien.pos
        alien.started = True
    if keyboard.f:
        alien.points += 99
        alien.level = 2
    # start and stop
    if alien.started:
        cat.x -= 7
        dim.x -= 7


    # enimes
    if dim.right < 0:
        dim.right = 100
    if cat.right < 0:
        cat.left = 1000
    if mine.right < 0:
        mine.right = 1000

    if mine2.top < 0:
        mine2.top = 1000

    #if mine3.top < 0:
        #mine3.top = 5000

    if zom.right < 0:
        zom.right = 1000

    if pigm.right < 0:
        pigm.right = 1000

    if cat.colliderect(alien):
        alien.gameover = True


pgzrun.go()
