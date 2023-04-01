import customtkinter
from tkinter import *
import cv2
import time
import random
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)


feelings = ['0']*4

m = 0

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry('500x350')
meeting_room = customtkinter.CTk()
meeting_room.geometry('500x350')
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
            time.sleep(0.01)
        main_frame.destroy()
        before_meetng_room()

    button_sub = customtkinter.CTkButton(master = main_frame , text = 'submit' , command = read_feelings)
    button_sub.pack(pady = 12 , padx = 10)
    

def main_room_meeting():
    bfr = customtkinter.CTkFrame(master = root)
    bfr.pack(pady = 20 , padx = 60 , fill = 'both', expand = True)
    entery_feeling_1 = customtkinter.CTkEntry(master = bfr , placeholder_text = "chat box" , font = ("Comic Sans MS", 10, "bold") , width=250)
    entery_feeling_1.pack(pady = 12 , padx = 10)
    chat = ""
    def r():
        chat = entery_feeling_1.get()
        if chat == feelings[0]:
            img = cv2.imread("happy.png", cv2.IMREAD_COLOR)
            label = customtkinter.CTkLabel(master = bfr , text = chat , font = ("Comic Sans MS", 15, "bold"))
            label.pack(pady = 12 , padx = 10)
        elif chat == feelings[1]:
            img = cv2.imread("sleep.png", cv2.IMREAD_COLOR)
            label = customtkinter.CTkLabel(master = bfr , text = chat , font = ("Comic Sans MS", 15, "bold"))
            label.pack(pady = 12 , padx = 10)
            
        elif chat == feelings[2]:
            img = cv2.imread("worried .png", cv2.IMREAD_COLOR)
            label = customtkinter.CTkLabel(master = bfr , text = chat , font = ("Comic Sans MS", 15, "bold"))
            label.pack(pady = 12 , padx = 10)
        else:
            img = cv2.imread("angry.png", cv2.IMREAD_COLOR)
            label = customtkinter.CTkLabel(master = bfr , text = chat , font = ("Comic Sans MS", 15, "bold"))
            label.pack(pady = 12 , padx = 10)
        cv2.imshow("facetime!", img)
        cv2.waitkey(0)
    def e():
        bfr.destroy()
    button = customtkinter.CTkButton(master =bfr , text = 'exit' , command = r)
    button.pack(pady = 12 , padx = 10)
    button_login = customtkinter.CTkButton(master =bfr , text = 'send' , command = r)
    button_login.pack(pady = 12 , padx = 10)

def before_meetng_room():
    root.geometry('500x450')
    main_frame = customtkinter.CTkFrame(master = root)
    main_frame.pack(pady = 20 , padx = 60 , fill = 'both', expand = True)
    label = customtkinter.CTkLabel(master = main_frame , text = "your meeting will starts in" , font = Font_tuple)
    label.pack(pady = 12 , padx = 10)
    cnt = customtkinter.CTkLabel(master = main_frame , text = "10 secends" , font = Font_tuple)
    cnt.pack(pady = 12 , padx = 10)
    _label = customtkinter.CTkLabel(master = main_frame , text = "Don't make him angry, otherwise it will be very bad" , font =  ("Comic Sans MS", 13, "bold"))
    _label.pack(pady = 12 , padx = 10)
    progress = customtkinter.CTkProgressBar(master = main_frame)
    progress.pack(pady = 12 , padx = 10)
    for i in range(1,100 , 1):
        progress.set(i*0.01)
        root.update_idletasks()
        time.sleep(0.1)
    main_frame.destroy()
    main_room_meeting()
    



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
            time.sleep(0.01)
        
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