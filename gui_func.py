from tkinter import END, filedialog
from tkinter import *
from csv_reader import csv_reader
from md_writer import md_writer
    
def icon_formatter(file_loc):
    ic = PhotoImage(file= file_loc).subsample(6)
    return ic

def dir_expl(dest_field,btn_id):
    if(btn_id == 'csv'):
        f = filedialog.askopenfilename(
                filetypes=(
                    ('CSV Files', "*.csv"),
                )
                )
    else:
        f = filedialog.askdirectory()    

    #csvField.set(f)
    clearField(dest_field)
    write_field(dest_field,f)

    
def clearField(field_name):
    field_name.delete(0,END)

def write_field(field_name,text):
    field_name.insert(0,text)

def read_field(field_name):
    return field_name.get()

def init_convert(csv_loc,dest):
    md_writer(csv_reader(csv_loc),dest)