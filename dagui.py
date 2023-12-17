import tkinter as tk
from tkinter import *

import Spotipies
from Spotipies import *
import webscrap
from webscrap import *
import convert
from convert import *
import cleaner
from cleaner import *

def download():
    global url_var, file_location_var

    url = url_var.get()
    file_location = file_location_var.get()

    URLGET(url)
    Spotipies.main()
    
    webscrap.main()
    
    LOCGET(file_location)
    convert.main()
    
    cleaner.main()
    
window = tk.Tk()
window.title("Spotify Downloader")
window.config(bg='#6dd5b4')

Icon = PhotoImage(file='icon.png')
window.iconphoto(True,Icon)

url_var = tk.StringVar()
file_location_var = tk.StringVar()

url_label = tk.Label(window, text="Enter URL:",bg='#6dd5b4')
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(window, textvariable=url_var, width=30)
url_entry.grid(row=0, column=1, padx=10, pady=10)

file_location_label = tk.Label(window, text="Enter File Location:", bg='#6dd5b4')
file_location_label.grid(row=1, column=0, padx=10, pady=10)

file_location_entry = tk.Entry(window, textvariable=file_location_var, width=30)
file_location_entry.grid(row=1, column=1, padx=10, pady=10)

download_button = tk.Button(window, text="Download",relief='groove', command=download, bg='#6dd5b4')
download_button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()