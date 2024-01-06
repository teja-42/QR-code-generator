from tkinter import *
import pyqrcode
from PIL import ImageTk,Image

root=Tk()

def generate():
    n=name_e.get()
    l=link_e.get()
    file_name=n+".png"
    url=pyqrcode.create(l)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    c.create_window(200,450,window=image_label)

c=Canvas(root,width=400,height=600)
c.pack()

l=Label(root,text="QR code generator",fg='blue',font=('Arial',30))
c.create_window(200,50,window=l)

name=Label(root,text="Link name")
link=Label(root,text="Link")
c.create_window(200,100,window=name)
c.create_window(200,160,window=link)

name_e=Entry(root)
link_e=Entry(root)
c.create_window(200,130,window=name_e)
c.create_window(200,180,window=link_e)

b=Button(root,text="Generate QR code",command=generate)
c.create_window(200,230,window=b)

root.mainloop()