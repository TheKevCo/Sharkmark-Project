from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw
import time

image = True


# button functions
def open_file():
    global image
    file = askopenfilename()
    im = Image.open(file)
    print(im.format, im.size, im.mode)
    image_success = Label(text="File Uploaded Successfully",
                          fg='red',
                          font=("Arial", 12, "bold"), )
    image_success.grid(column=1, row=2)
    image = im


def add_watermark():
    global watermark_entry
    image_editable = ImageDraw.Draw(image)
    image_text = str(watermark_entry.get())
    image_editable.text((15, 15), image_text, (237, 230, 211))
    image.show()

# UI SETUP
window = Tk()
window.title('Watermark App')
window.config(padx=50, pady=50)
logo = PhotoImage(file="logo1.png")
canvas = Canvas(width=200, height=303)
canvas.create_image(100, 130, image=logo)
canvas.grid(column=1, row=0)

# Image Upload
image_label = Label(text="Image Upload:", font=("Arial", 12, "bold"))
image_label.grid(column=0, row=1)

# Browse + Upload Button
upload_button = Button(text="Upload", width=14, command=open_file)
upload_button.grid(column=2, row=1, padx=3, pady=3)

# Watermark Text
watermark = Label(text="Watermark Text:", font=("Arial", 12, "bold"))
watermark.grid(column=0, row=3)
watermark_entry = Entry(width=51)
watermark_entry.focus()
watermark_entry.grid(column=1, row=3, columnspan=2)

# Add Watermark Button
watermark_button = Button(text="Add Watermark", width=12, command=add_watermark)
watermark_button.grid(column=1, row=4)

window.mainloop()
