from tkinter import *
import time

WIDTH = 500
HEIGHT = 600
xVelocity = 3
yVelocity = 2

window = Tk()
window.title("space")
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background = PhotoImage(file='bg.png')
back = canvas.create_image(0,0,image=background,anchor=NW)

photo_image = PhotoImage(file='ufo.png')
re = photo_image.subsample(2, 2)
resized_image = re.subsample(2, 2)
my_image = canvas.create_image(0,0,image=resized_image,anchor=NW)

image_width = resized_image.width()
image_height = resized_image.height()

while True:
    coordinates = canvas.coords(my_image)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)


    window.update()
    time.sleep(0.01)




window.mainloop()
