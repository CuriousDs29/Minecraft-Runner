#Title screen
#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import time

w=Tk()
#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    q=Tk()
    q.title('main window')
    q.mainloop()

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='MinecraftRunner', fg='white', bg='#272727') #decorate it
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))




for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
w.mainloop()
#
#game
WIDTH = 1247
HEIGHT = 700
#player
alien = Actor("pl")
alien.gravity = 0
alien.points = 0
alien.gameover = False
alien.started = False
#blocks and enimes
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
    bg.draw()
    screen.draw.text(f"points: {alien.points}", (0,0))
    alien.draw()
    zom.draw()
    pigm.draw()
    cat.draw()
    if alien.gameover:
        screen.fill("red")
        screen.draw.text("GAME OVER", (200,200))


def update():
    alien.gravity += 1
    alien.y += alien.gravity
    if alien.bottom >= HEIGHT:
        alien.bottom = HEIGHT
        alien.gravity = 0
    if keyboard.up and alien.bottom == HEIGHT:
        alien.gravity = -30
        alien.started = True
        sounds.l.play()
    if keyboard.left:
        alien.x -= 5
        alien.started = True
    if keyboard.right:
        alien.x += 5
        alien.started = True
    if alien.started:
        pigm.x -= 10
        zom.x -= 10
        cat.x -= 10
        alien.points += 1

    if cat.right < 0:
        cat.left = 1000
    if zom.right < 0:
        zom.right = 1000
    if pigm.right < 0:
        pigm.right = 1000
    if cat.colliderect(alien):
        alien.gameover = True


