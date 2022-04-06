import tkinter as tk
from tkinter.filedialog import *
from gcodes import get_gcode
from mcodes import get_mcode


#tkinter sandbox
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
def clicked():
  Input = progname.get()
  FileName = str("filepath" + Input + ".txt")
  TextFile = open(FileName,"w")
  
def create_new():
  """Create a new .txt file to store the CNC code"""
  filepath = asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
  )

  program.insert(INSERT, f'O{filepath}')

  if not filepath:
    return

def add_line():
  with open(filepath, mode="a", encoding="utf-8") as output_file:
    text = txt_edit.get("1.0", tk.END)
    output_file.write(text)
  window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Create a CNC Program")

window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(2, minsize=100, weight=1)
window.geometry('600x400')

frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=1)
frm_buttons.grid(row=0, column=0, sticky="ns")


btn_createnew = tk.Button(frm_buttons, text="Create New Program", command=create_new)
btn_createnew.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

program = tk.Text(window)
#op_line.place(bordermode = OUTSIDE, height = 20, relwidth = 1, rely = .7 )
program.grid(row=0, column=2, sticky="nsew")
program.insert(INSERT,'%\n')

btn_x = tk.Button(frm_buttons, text = 'X-Coordinate')
btn_x.grid(row=2, column = 0, sticky = 'ew', padx = 5, pady = 5)
x_coor = tk.Text(window, height = 1, width = 20)
x_coor.grid(row = 2, column = 1, sticky = 'nsew')





window.mainloop()