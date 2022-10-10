from tkinter import *
from PIL import Image, ImageTk
import PIL


Zoom_Scale = 1
Image_1_Path = 'images/Temp.png'

def Zoomin():
    global Zoom_Scale
    Zoom_Scale = round(Zoom_Scale + 0.1, 2)

    if Zoom_Scale > 3:
        Zoom_Scale = Zoom_Scale + 1

def ZoomOut():
    global Zoom_Scale
    if Zoom_Scale != 0.1:
        Zoom_Scale = round(Zoom_Scale - 0.1, 2)
    else:
        print('Cannot Zoom out more!')

    if Zoom_Scale > 3:
        Zoom_Scale = Zoom_Scale - 1

class Application():
    def __init__(self):
        # create the canvas, size in pixels
        self.canvas = Canvas(width=1000, height=900)

        # pack the canvas into a frame/form
        self.canvas.pack(fill=BOTH, expand=True)

        self.ZoominButton = Button(root, text="Zoom in", command=Zoomin)
        self.ZoominButton.pack()
        self.ZoomOutButton = Button(root, text="Zoom Out", command=ZoomOut)
        self.ZoomOutButton.pack()

        # load the .gif image file
        self.Image_1 = PhotoImage(file=Image_1_Path).zoom(Zoom_Scale)

        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.ImageID_1 = self.canvas.create_image(0, 0, image=self.Image_1, anchor=NW)


    def Update(self):
        print(f' >[{Zoom_Scale}]< ')
        self.UpdateImages()
        self.canvas.after(500, ClockCycle)

    def UpdateImages(self):
        #print(f' > Updated Images', end='')
        try:
            image = Image.open(Image_1_Path)
            C_width = image.width
            C_height = image.height
            # print(f'     Current width({C_width}), height({C_height})')
            T_width = round(C_width * (Zoom_Scale))
            T_height = round(C_height * (Zoom_Scale))
            # print(f'       Target width({T_width}), height({T_height})')
            ResizedImage = image.resize((T_width, T_height))

            ResizedImage = image.resize((T_width, T_height))

            self.Image_1 = ImageTk.PhotoImage(ResizedImage)
        except PIL.UnidentifiedImageError as UnidentifiedImageError:
            print(UnidentifiedImageError)
        except OSError as OSE:
            print(OSE)



        self.canvas.itemconfig(self.ImageID_1, image=self.Image_1)





root = Tk()
root.geometry("+4790+830")
app = Application()


def ClockCycle():
    app.Update()
# run it ...
root.after(200, ClockCycle())
root.mainloop()