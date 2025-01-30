import asyncio
from googletrans import Translator, LANGUAGES
import pyttsx3
import speech_recognition as sr
from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage
from tkinter.ttk import Combobox
from tkinter import ttk 
import tkinter.font as tkFont

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\kamekazi\Desktop\Master_Python\GUI\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_value():
    exchange1 = monthchoosen_1.get()
    exchange2 = monthchoosen_3.get()
    monthchoosen_1.set(exchange2)
    monthchoosen_3.set(exchange1)

def translate_text():
    translator = Translator()
    input_text = entry_1.get("1.0", "end-1c")
    src_lang = monthchoosen_1.get()
    dest_lang = monthchoosen_3.get()
    src_lang_code = next((key for key, value in LANGUAGES.items() if value == src_lang), "auto")
    dest_lang_code = next((key for key, value in LANGUAGES.items() if value == dest_lang), "en")
    translated_text = asyncio.run(translate_async(translator, input_text, src_lang_code, dest_lang_code))
    entry_2.delete("1.0", "end")
    entry_2.insert("1.0", translated_text)

async def translate_async(translator, text, src, dest):
    result = await translator.translate(text, src=src, dest=dest)
    return result.text

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}\nName: {voice.name}\nLang: {voice.languages}\n")

def speak_text():
    engine = pyttsx3.init()
    text = entry_2.get("1.0", "end-1c").strip()
    if not text:
        return
    selected_lang = monthchoosen_3.get().lower()
    voices = engine.getProperty('voices')
    chosen_voice = None
    for voice in voices:
        if selected_lang == "hindi" and "hi-in" in voice.id.lower():
            chosen_voice = voice.id
            break
        elif selected_lang == "english" and "en" in voice.id.lower():
            chosen_voice = voice.id
            break
    if chosen_voice:
        engine.setProperty('voice', chosen_voice)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def speak_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said: ", text)
            entry_1.delete("1.0", "end")
            entry_1.insert("1.0", text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return None

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
    text="Translator by Kazi ⭐",
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

monthchoosen_1 = ttk.Combobox(window, width=20,state="readonly", font="Verdana 16 bold")
monthchoosen_1['values'] = list(LANGUAGES.values())
monthchoosen_1.current(57)
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

monthchoosen_3 = Combobox(window, width=20,state="readonly", font="Verdana 16 bold")
monthchoosen_3['values'] = list(LANGUAGES.values())
monthchoosen_3.current(83)
monthchoosen_3.place(x=238.0, y=84.0, width=159.0, height=47.0)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    background='#1e1e1e',
    command=get_value
)
button_3.place(x=181.0, y=84.0, width=50.0, height=50.0)

font_style = tkFont.Font(family="Helvetica", size=14, weight="bold")

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
    font=font_style
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
    font=font_style
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
    command=speak_to_text,
    relief="flat",
    background="#1e1e1e"
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
    command=speak_text,
    relief="flat",
    background="#1e1e1e"
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
    command=translate_text,
    relief="flat",
    background="#1e1e1e"
)
button_6.place(
    x=226.0,
    y=711.0,
    width=159.0,
    height=60.0
)

window.resizable(False, False)
window.mainloop()