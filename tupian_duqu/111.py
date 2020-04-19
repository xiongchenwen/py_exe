import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

Filepath = filedialog.askopenfilename() #获得选择好的文件


print('Filepath:',Filepath)
