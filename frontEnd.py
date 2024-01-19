#!/usr/bin/python3

import os
import tkinter as tk
import logging
from tkinter import scrolledtext
from backEnd import is_valid_url
from tkinter import messagebox

# Configure Logging
logging_directory = r'C:\ytAudio'
logging_file = 'ytAudio.log'
logs = os.path.join(logging_directory, logging_file)
os.makedirs(logging_directory, exist_ok=True)

if not os.path.exists(logs):
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

##### Stream Menus
high_menu = tk.Frame(window, width=150, height=200, bg="lightblue")
high_menu.grid(row=2, column=0, pady=20, padx=20, sticky=tk.W)

medium_menu = tk.Frame(window, width=150, height=200, bg="green")
medium_menu.grid(row=2, column=1, pady=20, padx=20)

low_menu = tk.Frame(window, width=150, height=200, bg="brown")
low_menu.grid(row=2, column=2, pady=20, padx=20)

def process_url():
    url = url_entry.get()
    # check if the entered value is a valid url
    if is_valid_url(url):
        logging.info("The entered URL is a valid, youtube url")
    else:
        logging.error("Invalid URL... Please enter a valid youtube URL...")
        messagebox.showerror("Invalid URL...", "Please enter a valid youtube URL...")

# def function_to_run_multiple_functions for my capture button

#### Capture button
capture_button = tk.Button(window, text="Process", command=process_url)
capture_button.grid(row=1, column=2, pady=10, padx=20, sticky=tk.EW)

window.mainloop()