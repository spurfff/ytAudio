#!/usr/bin/python3

import tkinter as tk
from backEnd import is_valid_url
from tkinter import messagebox


# the UI for my ytAudio App

##### The main Window
window = tk.Tk()
window.title("ytAudio")
window.geometry("400x200")

# Configure rows and columns to retain size
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)


##### Title
label = tk.Label(window, text="ytAudio")
label.grid(row=0, column=1, pady=20, padx=20)

##### Enter url field
url_label = tk.Label(window, text="Enter URL:")
url_label.grid(row=1, column=0, pady=10, padx=20, sticky=tk.W)

url_entry = tk.Entry(window, width=30)
url_entry.grid(row=1, column=1, pady=10, padx=20, sticky=tk.EW)

def process_url():
    entered_url = url_entry.get()
    # check if the entered value is a valid url
    if is_valid_url(entered_url):
        messagebox.showinfo("Valid URL!", f"The Entered URL is valid: {entered_url}")
        video_url = entered_url
    else:
        messagebox.showerror("Invalid URL...", "Please enter a valid youtube URL...")

    


#### Capture button
caputure_button = tk.Button(window, text="Process", command=process_url)
caputure_button.grid(row=2, column=1, columnspan=1, pady=10, padx=10, sticky=tk.EW)

window.mainloop()