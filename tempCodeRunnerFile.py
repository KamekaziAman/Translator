from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage
from tkinter.ttk import Combobox
import tkinter.font as tkFont  # Import tkinter font module

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kamekazi\Desktop\Master_Python\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("411x791")
window.configure(bg="#FFFFFF")
window.title("Translator")
window.iconbitmap("assets/frame0/icon.ico")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=791,
    width=411,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    205.0,
    395.0,
    image=image_image_1
)

canvas.create_text(
    11.0,
    17.0,
    anchor="nw",
    text="Translator by Kazi",
    fill="#E2E2E2",
    font=("ExtraBold", 30 * -1)
)

canvas.create_rectangle(
    -4.0,
    64.0,
    423.99997758813515,
    68.63234226595517,
    fill="#E2E2E2",
    outline=""
)

# Combobox for Button 1
monthchoosen_1 = Combobox(window, width=20)  # Adjust width as needed
monthchoosen_1['values'] = ('English', 'Hindi')  # Set default values
monthchoosen_1.current(0)  # Set default to 'English'
monthchoosen_1.place(x=13.0, y=84.0, width=159.0, height=47.0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(x=181.0, y=84.0, width=50.0, height=50.0)

# Combobox for Button 3
monthchoosen_3 = Combobox(window, width=20)  # Adjust width as needed
monthchoosen_3['values'] = ('English', 'Hindi')  # Set default values
monthchoosen_3.current(1)  # Set default to 'Hindi'
monthchoosen_3.place(x=238.0, y=84.0, width=159.0, height=47.0)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=181.0, y=84.0, width=50.0, height=50.0)

# Set font for Text entries
font_style = tkFont.Font(family="Helvetica", size=14, weight="bold")  # Customize font style

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    205.5,
    280.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font_style  # Set the font style
)
entry_1.place(
    x=37.0,
    y=149.0,
    width=337.0,
    height=261.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    205.5,
    558.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=font_style  # Set the font style
)
entry_2.place(
    x=37.0,
    y=427.0,
    width=337.0,
    height=261.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=30.0,
    y=706.0,
    width=70.0,
    height=70.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=123.0,
    y=706.0,
    width=70.0,
    height=70.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=226.0,
    y=711.0,
    width=159.0,
    height=60.0
)

window.resizable(False, False)
window.mainloop()