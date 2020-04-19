import dxfgrabber
import tkinter as tk
from tkinter import filedialog
win = tk.Tk()
win.withdraw()
dxf=dxfgrabber.readfile(filedialog.askopenfilename())
for e in dxf.entities:
    if e.dxftype=='LINE':
        f=[e.start[0] for e in dxf.entities]
        g=[e.end[0] for e in dxf.entities]
        h=[e.start[1] for e in dxf.entities]
        i=[e.end[1] for e in dxf.entities]
import matplotlib.pyplot as plt
x=f,g
y=h,i
plt.plot(x,y)
plt.show()
print(type(x))
