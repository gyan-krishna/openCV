# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Mon Jun 14 12:30:10 2021
@author: Gyan Krishna

Topic:
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.wm_title("Tkinter window")
root.geometry("800x600")

load = Image.open("mario_raw.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.grid(row = 0, column = 0)

root.mainloop()