"""
Created on Tue Feb  5 15:32:45 2019

@author: samgorse
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()

win.title ("Aegis")

win.minsize(width=850, height=850)
win.maxsize(width=1080, height=1080)

action1 = ttk.Button (win, text = "Search Active Directory")
action1.grid (column = 3, row = 3)

action2 = ttk.Button (win, text = "Print Report")
action2.grid (column = 4, row = 3)

ttk.Label (win, text = "Report:").grid (column = 5, row = 4, padx = 10, pady = 10) 

search = tk.StringVar()
searchBox = ttk.Entry (win, width = 20, textvariable = search)
searchBox.grid (column = 5, row = 8)

action3 = ttk.Button (win, text = "Search")
action3.grid (column = 6, row = 8)

scrolW = 100
scrolH = 20
scr = scrolledtext.ScrolledText (win, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid (column = 5, columnspan = 8)

ttk.Label (win, text = "Weak Protection:").grid (column = 1, row = 4, padx = 10, pady = 10) 

weak = tk.StringVar()
weakProtection = ttk.Entry (win, width = 20, textvariable = weak)
weakProtection.grid (column = 1, row = 5)

ttk.Label (win, text = "Protected:").grid (column = 1, row = 6, padx = 10, pady = 10)

strong = tk.StringVar()
strongProtection = ttk.Entry (win, width = 20, textvariable = strong)
strongProtection.grid (column = 1, row = 7)

win.mainloop()