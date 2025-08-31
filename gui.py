from tkinter import *
import tkinter as tk
from tkinter import END, filedialog
from gui_func import icon_formatter, dir_expl, read_field, init_convert


def gui():
    #root frame
    root = tk.Tk()
    root.title('mtg_csv_to_md')
    #Window Size
    root.geometry("500x200")

    #Init component dimensions
    btn_w = 25
    btn_h = 25
    wide_btn_w = 40
    wide_btn_h = 5
    fieldWidth = 55

    #Text labels
    tk.Label(root, text='CSV file:').grid(row=0)
    tk.Label(root, text='Target Directory:').grid(row=1)
    #Input Fields + location
    csvField = tk.Entry(root,width=fieldWidth)
    destField = tk.Entry(root,width=fieldWidth)
    csvField.grid(row=0, column=1)
    destField.grid(row=1, column=1)

    i = icon_formatter('icons/folder.png')
    #border = LabelFrame(root, bd = 6, bg = "black")
    #Directory button init
    tk.Button(root, image=i,width=btn_w,height=btn_h, relief=FLAT, command=lambda:dir_expl(csvField,'csv')).grid(row=0,column=2)
    tk.Button(root, image=i,width=btn_w,height=btn_h, relief=FLAT, command=lambda:dir_expl(destField,'dst')).grid(row=1,column=2)

    tk.Button(root, text='Convert',width=wide_btn_w, relief=FLAT, command=lambda:init_convert(read_field(csvField),read_field(destField))).grid(row=3,column=1)

    mainloop()


if __name__=="__gui__":
    gui()