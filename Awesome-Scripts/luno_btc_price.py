import tkinter as tk
from tkinter import ttk
import urllib.request
import json

currency = "MYR" # there are IDR, NGN, ZAR and MYR

def get_luno():
	req = urllib.request.urlopen("https://api.mybitx.com/api/1/ticker?pair=XBT" + currency)
	x = json.loads(req.read().decode("utf-8"))
	req.close()
	return x

def refresh_price():
	aLable.configure(text="Ask price: " + get_luno()["ask"])

win = tk.Tk()
win.title("Bitcoin price in " + currency)

aLable = ttk.Label(win, text="Ask price: " + get_luno()["ask"])
aLable.grid(column=0, row=0, padx=8, pady=4)

action = ttk.Button(win, text="Refresh", command=refresh_price)
action.grid(column=0, row=1, padx=8, pady=4)

win.mainloop()
