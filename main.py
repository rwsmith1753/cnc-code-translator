import tkinter as tk
from tkinter.filedialog import *
#from gcodes import get_gcode
#from mcodes import get_mcode
import gcodes2
import mcodes2


orow = 0
newrow = orow + 1
svrow = newrow + 1
grow = svrow + 1
xrow = grow + 1
yrow = xrow + 1
srow = yrow + 1
frow = srow + 1
mrow = frow + 1
nlrow = mrow + 1
clrow = nlrow + 1




def open_file():
  """Open a file for editing."""
  filepath = askopenfilename(
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )
  if not filepath:
    return
  program.delete("1.0", tk.END)
  with open(filepath, mode="r", encoding="utf-8") as input_file:
    text = input_file.read()
    program.insert(tk.END, text)
  window.title(f"CNC Translator - {filepath}")


#==Create new program, and insert program name
def create_new():
  """Create a new .txt file to store the CNC code"""
  filepath = asksaveasfilename(

    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
  )
  if not filepath:
    return
  with open(filepath, 'w+'):
    pathsplit = filepath.split('/')
    filename = pathsplit[-1].split('.')
    program.insert(tk.INSERT, f'O{filename[0]}\n')
    prog = program.get(1.0, 'end')
    filepath.write(prog)
    filepath.close()


def save_file():
  with open(filepath, 'w+'):
    prog = program.get(1.0, 'end')
    filepath.write(prog)
    filepath.close()


def add_g():
  selg = lst_g.get(lst_g.curselection())
  if selg == 'None':
    pass
  else:
    g = selg.split(': ')
    cline.insert(tk.INSERT, g[0])

  
  
def add_x():
  x = x_coor.get('1.0', 'end-1c')
  if isinstance(x,int):
    cline.insert(tk.INSERT, f'X{x}.')  
  else:
    cline.insert(tk.INSERT, f'X{x}')
  x_coor.delete('1.0', 'end-1c')

def add_y():
  y = y_coor.get('1.0', 'end-1c')
  if isinstance(y,int):
    cline.insert(tk.INSERT, f'Y{y}.')  
  else:
    cline.insert(tk.INSERT, f'Y{y}')
  y_coor.delete('1.0', 'end-1c')

def add_s():
  s = speed.get('1.0', 'end-1c')
  cline.insert(tk.INSERT, f'S{s}')
  speed.delete('1.0', 'end-1c')

def add_f():
  f = feed.get('1.0', 'end-1c')
  cline.insert(tk.INSERT, f'F{f}')
  feed.delete('1.0', 'end-1c')
  

def add_m():
  selm = lst_m.get(lst_m.curselection())
  if selm == 'None':
    pass
  else:
    m = selm.split(': ')
    cline.insert(tk.INSERT, m[0])

def new_line():
  code = cline.get('1.0', 'end-1c')
  program.insert(tk.INSERT, f'{code}\n')
  cline.delete('1.0', 'end-1c')




  
#===Window Config  
window = tk.Tk()
window.title('CNC Translator')
#window.rowconfigure([0,1,2,3,4,5,6,7], minsize = 42)
#window.columnconfigure(0, minsize = 200)
window.geometry('800x800')

#===Button Config
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=1)
frm_buttons.columnconfigure(0, minsize = 300)
frm_buttons.grid(column=0, rowspan = 12, sticky="nsew")

#===Text Box Config
txt_box = tk.Frame(window, bd=1)
txt_box.rowconfigure(0, minsize = 42)
txt_box.grid(column=1, row = 3, rowspan = 12, sticky="nsew")

#=====Text Window
program = tk.Text(window)
program.grid(column=2, row = 0, rowspan = 12, sticky="nsw")
program.insert(tk.INSERT,'%\n')

#=====Open Program
btn_open = tk.Button(frm_buttons, text = 'Open Program', command = open_file)
btn_open.grid(column = 0, row = orow, stick = 'nsew', padx = 5, pady = 5)

#=====Create New Program
btn_createnew = tk.Button(frm_buttons, text="Create New Program", command=create_new)
btn_createnew.grid(column=0, row=newrow, sticky="nsew", padx=5, pady=5)

#=====Save Program
btn_save = tk.Button(frm_buttons, text = 'Save Program', command = save_file)
btn_save.grid(column = 0, row = svrow, sticky = 'nsew', padx = 5, pady = 5)

#=====G Code list
#g = StringVar()
#g.set(gcodes2.gcode_list[1])
lst_g = tk.Listbox(frm_buttons)
lst_g.grid(column = 0, row = grow, sticky = 'new')
lst_g.insert(tk.END, 'None')
for i in gcodes2.gcode_list:
  lst_g.insert(tk.END, i)
lst_g.select_set(0)
btn_g = tk.Button(txt_box, text = 'Insert G-Code', command = add_g)
btn_g.grid(column = 1, row = grow, sticky = 'new', padx = 5, pady = 5)

#=====Code to insert
# cline = tk.Text(txt_box, height = 1, width = 20)
# cline.grid(column = 1, row = 4, sticky = 'nsew', padx = 5, pady = 8)

#=====X Coordinate
x_coor = tk.Text(txt_box, height = 1, width = 20)
x_coor.grid(column = 1, row = xrow, sticky = 'new', padx = 5, pady = 8)
btn_x = tk.Button(frm_buttons, text = 'X-Coordinate', command = add_x)
btn_x.grid(column = 0, row=xrow, sticky = 'nsew', padx = 5, pady = 5)


#=====Y Coordinate
y_coor = tk.Text(txt_box, height = 1, width = 20)
y_coor.grid(column = 1, row = yrow, sticky = 'new', padx = 5, pady = 8)
btn_y = tk.Button(frm_buttons, text = 'Y-Coordinate', command = add_y)
btn_y.grid(column = 0, row=yrow, sticky = 'nsew', padx = 5, pady = 5)

#=====Speed
speed = tk.Text(txt_box, height = 1, width = 20)
speed.grid(column = 1, row = srow, sticky = 'new', padx = 5, pady = 8)
spd_btn = tk.Button(frm_buttons, text = 'Speed (RPM)', command = add_s)
spd_btn.grid(column = 0, row=srow, sticky = 'nsew', padx = 5, pady = 5)

#=====Feed
feed = tk.Text(txt_box, height = 1, width = 20)
feed.grid(column = 1, row = frow, sticky = 'new', padx = 5, pady = 8)
fd_btn = tk.Button(frm_buttons, text = 'Feed (Inch/Rev)', command = add_f)
fd_btn.grid(column = 0, row=frow, sticky = 'nsew', padx = 5, pady = 5)

#=====M Code
lst_m = tk.Listbox(frm_buttons)
lst_m.grid(column = 0, row = mrow, sticky = 'new')
lst_m.insert(tk.END, 'None')
for i in mcodes2.mcode_list:
  lst_m.insert(tk.END, i)
btn_m = tk.Button(txt_box, text = 'Insert M-Code', command = add_m)
btn_m.grid(column = 1, row = mrow, sticky = 'new')

#=====New line
btn_NL = tk.Button(txt_box, text = 'New Line', command = new_line)
btn_NL.grid(column = 1, row = nlrow, sticky = 'nsew', padx = 5, pady = 8)

#=====Code to insert
cline = tk.Text(txt_box, height = 1, width = 20)
cline.grid(column = 1, row = clrow, sticky = 'nsew', padx = 5, pady = 8)



window.mainloop()