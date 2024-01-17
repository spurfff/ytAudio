#!/usr/bin/python3

import os
import tkinter as tk
from backEnd import is_valid_url
import logging
from tkinter import messagebox

# Configure Logging
logging_directory = r'C:\ytAudio'
logging_file = 'ytAudio.log'
logs = os.path.join(logging_directory, logging_file)
os.makedirs(logging_directory, exist_ok=True)

with open(logs, 'w') as file:
    file.write("Log file created")

logging.basicConfig(filename=logs, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# the UI for my ytAudio App

##### The main Window
window = tk.Tk()
window.title("ytAudio")
window.geometry("550x450")

# Configure rows and columns to retain size
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)


##### Title
label = tk.Label(window, text="ytAudio", font=("Helvetica", 16))
label.grid(row=0, column=0, pady=20, padx=20)

##### Enter url field
url_label = tk.Label(window, text="Enter URL:")
url_label.grid(row=1, column=0, pady=10, padx=20, sticky=tk.W)

url_entry = tk.Entry(window, width=30)
url_entry.grid(row=1, column=1, pady=10, padx=20, sticky=tk.EW)

stream_menu_high = tk.Frame(window, width=150, height=200, bg="lightblue")
stream_menu_high.grid(row=2, column=0, pady=20, padx=20, sticky=tk.W)

stream_menu_medium = tk.Frame(window, width=150, height=200, bg="green")
stream_menu_medium.grid(row=2, column=1, pady=20, padx=20)

stream_menu_low = tk.Frame(window, width=150, height=200, bg="brown")
stream_menu_low.grid(row=2, column=2, pady=20, padx=20)

def process_url():
    entered_url = url_entry.get()
    # check if the entered value is a valid url
    if is_valid_url(entered_url):
        logging.info("Success!", "You did it buddy...")
    else:
        logging.error("Invalid URL...", "Please enter a valid youtube URL...")
        messagebox.showerror("Invalid URL...", "Please enter a valid youtube URL...")

#### Capture button
caputure_button = tk.Button(window, text="Process", command=process_url)
caputure_button.grid(row=1, column=2, pady=10, padx=20, sticky=tk.EW)

window.mainloop()