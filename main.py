import tkinter as tk
from tkinter.filedialog import *
from gcodes import get_gcode
from mcodes import get_mcode


#==Unused
def open_file():
  """Open a file for editing."""
  filepath = askopenfilename(
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )
  if not filepath:
    return
  txt_edit.delete("1.0", tk.END)
  with open(filepath, mode="r", encoding="utf-8") as input_file:
    text = input_file.read()
    txt_edit.insert(tk.END, text)
  window.title(f"Simple Text Editor - {filepath}")

#==Unused
def clicked():
  Input = progname.get()
  FileName = str("filepath" + Input + ".txt")
  TextFile = open(FileName,"w")

#==Create new program, and insert program name
def create_new():
  """Create a new .txt file to store the CNC code"""
  filepath = asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
  )

  program.insert(INSERT, f'O{filepath}\n')

  if not filepath:
    return

#==Unused
def add_line():
  with open(filepath, mode="a", encoding="utf-8") as output_file:
    text = txt_edit.get("1.0", tk.END)
    output_file.write(text)
  window.title(f"Simple Text Editor - {filepath}")

def add_x():
  x = x_coor.get('1.0', 'end-1c')
  cline.insert(INSERT, f'X{x}')
  x_coor.delete('1.0', 'end-1c')

def add_y():
  y = y_coor.get('1.0', 'end-1c')
  cline.insert(INSERT, f'Y{y}')
  y_coor.delete('1.0', 'end-1c')

def new_line():
  code = cline.get('1.0', 'end-1c')
  program.insert(INSERT, f'{code}\n')
  cline.delete('1.0', 'end-1c')


  
#===Window Config  
window = tk.Tk()
window.title("Create a CNC Program")
#window.rowconfigure([0,1,2,3,4,5,6,7], minsize = 42)
#window.columnconfigure([0,1,2], weight = 0)
window.geometry('600x400')

#===Button Config
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=1)
frm_buttons.grid(column=0, rowspan = 8, sticky="nsew")

#===Text Box Config
txt_box = tk.Frame(window, relief = tk.RAISED, bd=1)
txt_box.rowconfigure(0, minsize = 42)
txt_box.grid(column=1, row = 0, rowspan = 8, sticky="nsew")

#=====Text Window
program = tk.Text(window)
program.grid(column=2, row = 0, rowspan = 8, sticky="nsw")
program.insert(INSERT,'%\n')

#=====Create New Program
btn_createnew = tk.Button(frm_buttons, text="Create New Program", command=create_new)
btn_createnew.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

#=====Code to insert
cline = tk.Text(txt_box, height = 1, width = 20)
cline.grid(column = 1, row = 4, sticky = 'nsew', padx = 5, pady = 8)

#=====X Coordinate
x_coor = tk.Text(txt_box, height = 1, width = 20)
x_coor.grid(column = 1, row = 1, sticky = 'new', padx = 5, pady = 8)
btn_x = tk.Button(frm_buttons, text = 'X-Coordinate', command = add_x)
btn_x.grid(column = 0, row=1, sticky = 'nsew', padx = 5, pady = 5)


#=====Y Coordinate
y_coor = tk.Text(txt_box, height = 1, width = 20)
y_coor.grid(column = 1, row = 2, sticky = 'new', padx = 5, pady = 8)
btn_y = tk.Button(frm_buttons, text = 'Y-Coordinate', command = add_y)
btn_y.grid(column = 0, row=2, sticky = 'nsew', padx = 5, pady = 5)


#=====New line
btn_NL = tk.Button(txt_box, text = 'New Line', command = new_line)
btn_NL.grid(column = 1, row = 3, sticky = 'nsew', padx = 5, pady = 8)

#=====Code to insert
cline = tk.Text(txt_box, height = 1, width = 20)
cline.grid(column = 1, row = 4, sticky = 'nsew', padx = 5, pady = 8)



window.mainloop()