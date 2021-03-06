import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def addApp():
  filename = filedialog.askopenfilename(initialdir="/", title="Select File",
  filetypes=(("executables","*.exe"), ("all files", "*.*")))


canvas = tk.Canvas(root, height=700, width=700, bg="red")
canvas.pack()

frame = tk.Frame(root, bg="blue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="blue", bg="red", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="blue", bg="red")


runApps.pack()

root.mainloop()