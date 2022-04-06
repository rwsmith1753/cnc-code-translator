import re
from itertools import groupby
# import numpy as np
# import matplotlib.pyplot as plt
import os
from subprocess import call
from gcodes import get_gcode
from mcodes import get_mcode
from classes import *
from colorama import Fore, Back, Style




#clear screen
_ = call('clear' if os.name == 'posix' else 'cls')
#import CNC file
cnc = open("cncsample.txt", 'r')
program = cnc

pos = {}
l = 0
zcom = ''
xcom = ''
x = 0.0
z = 0.0
cmd = ''
feed = 0
speed = 0

for line in program:
  g = ''
  m = ''
  l += 1
  lst = [''.join(i) for _, i in groupby(line, str.isalpha)]
  if line[0] == '%':
    print(f'{l}: {line.strip()}')
  elif line[0] == 'O':
    print(f'{l}: ' + Fore.BLUE + Style.BRIGHT + 'Program Name --> {line.strip()}' + Style.RESET_ALL)
  elif line[0] == '(':
    print(f'{l}: ' + Fore.MAGENTA + Style.DIM + f'==={line.strip()}===' + Style.RESET_ALL)
  elif line[0] == 'M':
    m = lst[0] + str(lst[1].strip())
    print(f'{l}: ' + Fore.RED + f'!!! {get_mcode(m)} !!!' + Style.RESET_ALL)
  else:
    for i in range(len(lst)):

      if lst[i] == 'X':
        xcom = (f'X={lst[i+1].strip()}')
        x=lst[i+1].strip()
      elif lst[i] == 'Z':
        zcom = (f'Z={lst[i+1].strip()}')
        z=lst[i+1].strip()
      elif lst[i] == 'G':
        g = lst[i] + str(lst[i+1])
      elif lst[i] == 'S':
        speed = ': ' + color.CYAN + f'Spindle Speed: ' + color.END + f'{lst[i+1].strip()} RPM'
      elif lst[i] == 'F':
        feed = ': ' + color.BLUE + 'Feed Rate: ' + color.END + f'{lst[i+1].strip()} IN/REV'
      elif lst[i] == 'T':
        tool = ': ' + color.UNDERLINE + f'Tool/Offset #: {lst[i+1].strip()}' + color.END 
      elif lst[i] == 'M':
        m = lst[i] + str(lst[i+1].strip())
      elif lst[i] == 'N':
        pass
      pos.update({float(z) if z != '' else 0:float(x) if x != '' else 0})
      cmd = [xcom,zcom]

#=====PRINT OPERATION=========== 
    printcoor = ''
    if 'X' in line:
      printcoor = color.GREEN + 'Travel to: ' + color.END + xcom
    elif 'Z' in line: 
      printcoor = color.GREEN + 'Travel to: ' + color.END + zcom
    if 'X' in line and 'Z' in line:
      printcoor = color.GREEN + 'Travel to: ' + color.END + xcom + ", " + zcom
      
    print(f"{l}: {get_gcode(g) + ' ' if g != '' else ''}{tool if 'T' in line else ''}{speed if 'S' in line else ''}{printcoor}{feed if 'F' in line else ''}{'  --> ' + get_mcode(m)  if m != '' else ''}")
#=========================


#print(pos)
#print(pos.keys(),pos.values())

#=====Plot

# plt.scatter(pos.keys(),pos.values(), s=100)
# plt.plot(pos.keys(),pos.values())
# plt.title("Part Profile")
# plt.xlabel("z")
# plt.ylabel('x')
# plt.show()







