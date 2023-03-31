import customtkinter
import time
import random
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

# pick an animated gif file you have in the working directory


class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'C:\\your\\path\\to\\file'

feelings = ['0']*4

m = 0

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry('500x350')
Font_tuple = ("Comic Sans MS", 24, "bold")


        



def main_screen():
    root.geometry('500x450')
    main_frame = customtkinter.CTkFrame(master = root)
    main_frame.pack(pady = 20 , padx = 60 , fill = 'both', expand = True)

    

    label = customtkinter.CTkLabel(master = main_frame , text = "manage the meeting codes" , font = Font_tuple)
    label.pack(pady = 12 , padx = 10)

    entery_feeling_1 = customtkinter.CTkEntry(master = main_frame , placeholder_text = "enter your code to make your bot laught" , font = ("Comic Sans MS", 10, "bold") , width=250)
    entery_feeling_1.pack(pady = 12 , padx = 10)

    entery_feeling_2 = customtkinter.CTkEntry(master = main_frame , placeholder_text = "enter your code to make your bot cry" , font = ("Comic Sans MS", 10, "bold") , width=250)
    entery_feeling_2.pack(pady = 12 , padx = 10)

    entery_feeling_3 = customtkinter.CTkEntry(master = main_frame , placeholder_text = "enter your code to make your bot sleep" , font = ("Comic Sans MS", 10, "bold") , width=250)
    entery_feeling_3.pack(pady = 12 , padx = 10)

    entery_feeling_4 = customtkinter.CTkEntry(master = main_frame , placeholder_text = "enter your code to make your bot became sceard" , font = ("Comic Sans MS", 10, "bold") , width=250)
    entery_feeling_4.pack(pady = 12 , padx = 10)

    def read_feelings():
        feelings[0] = entery_feeling_1.get()
        feelings[1] = entery_feeling_2.get()
        feelings[2] = entery_feeling_3.get()
        feelings[3] = entery_feeling_4.get()
        label_ = customtkinter.CTkLabel(master = main_frame , text = "your submetion was complet, please wait we are working on it" , font = ("Comic Sans MS", 12, "bold"))
        label_.pack(pady = 12 , padx = 10)
        progress = customtkinter.CTkProgressBar(master = main_frame)
        progress.pack(pady = 12 , padx = 10)
        for i in range(1,100 , 1):
            progress.set(i*0.01)
            root.update_idletasks()
            time.sleep(0.1)
        time.sleep(3)
        main_frame.destroy()
        before_meetng_room()

    button_sub = customtkinter.CTkButton(master = main_frame , text = 'submit' , command = read_feelings)
    button_sub.pack(pady = 12 , padx = 10)
    
        


def before_meetng_room():
    bfr = customtkinter.CTkFrame(master = root)
    bfr.pack(pady = 20 , padx = 60 , fill = 'both', expand = True)
    label = customtkinter.CTkLabel(master = bfr , text = "your meeting will starts in" , font = Font_tuple)
    label.pack(pady = 12 , padx = 10)
    cnt = customtkinter.CTkLabel(master = bfr , text = "30 secends" , font = Font_tuple)
    cnt.pack(pady = 12 , padx = 10)
    _label = customtkinter.CTkLabel(master = bfr , text = "Don't make him angry, otherwise it will be very bad" , font =  ("Comic Sans MS", 13, "bold"))
    _label.pack(pady = 12 , padx = 10)


        
    








def login():
    user = entery_1.get()
    password = entery_2.get()
    if user == 'nemoxer' and password == '1234':
        label = customtkinter.CTkLabel(master = login_screen , text = "login was sussece full" , font = ("Comic Sans MS", 15, "bold"))
        label.pack(pady = 12 , padx = 10)
        progress = customtkinter.CTkProgressBar(master = login_screen)
        progress.pack(pady = 12 , padx = 10)
        for i in range(1,100 , 1):
            progress.set(i*0.01)
            root.update_idletasks()
            time.sleep(0.1)
        time.sleep(3)
        login_screen.destroy()
        main_screen()
    

login_screen = customtkinter.CTkFrame(master = root)
login_screen.pack(pady = 20 , padx = 60 , fill = 'both', expand = True)

label = customtkinter.CTkLabel(master = login_screen , text = "login system to GUI-AI" , font = Font_tuple)
label.pack(pady = 12 , padx = 10)

entery_1 = customtkinter.CTkEntry(master = login_screen , placeholder_text = "enter your user name" , font = ("Comic Sans MS", 15, "bold") , width=200)
entery_1.pack(pady = 12 , padx = 10)

entery_2 = customtkinter.CTkEntry(master = login_screen ,show = '*', placeholder_text = "enter your password" , font = ("Comic Sans MS", 15, "bold") , width=200)
entery_2.pack(pady = 12 , padx = 10)

button_login = customtkinter.CTkButton(master = login_screen , text = 'login' , command = login)
button_login.pack(pady = 12 , padx = 10)


root.mainloop()