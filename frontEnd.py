#!/usr/bin/python3

import tkinter as tk
#import backEnd
from tkinter import messagebox


# the UI for my ytAudio App

##### The main Window
window = tk.Tk()
window.title("ytAudio")
window.geometry("400x200")


##### Title
label = tk.Label(window, text="ytAudio")
label.grid(row=0, column=1, pady=20)

##### Enter url field
url_label = tk.Label(window, text="Enter URL: ")
url_label.grid(row=1, column=0, pady=20, padx=10, sticky=tk.W)

url_entry = tk.Entry(window, width=40)
url_entry.grid(row=1, column=1, pady=20, padx=20, sticky=tk.EW)



window.mainloop()