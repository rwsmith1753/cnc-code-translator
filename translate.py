from itertools import groupby
import matplotlib.pyplot as plt
import os
from subprocess import call
from gcodes import get_gcode
from mcodes import get_mcode
from colorama import Fore, Style

def Translate():
  #clear screen
  _ = call('clear' if os.name == 'posix' else 'cls')
  
  #import CNC file
  cnc = open("cncsample.txt", 'r')
  program = cnc
  
  linDic = {}
  rapDic = {}
  l = 0
  zcom = ''
  xcom = ''
  Rx = 0.0
  Rz = 0.0
  Lx = 0.0
  Lz = 0.0
  cmd = ''
  feed = 0
  speed = 0
  
  
  for line in program:
    g = ''
    m = ''
    l += 1
    rapid = 'OFF'
    lst = [''.join(i) for _, i in groupby(line, str.isalpha)]
    if line[0] == '%':
      print(f'{l}: {line.strip()}')
    elif line[0] == 'O':
      print(f'{l}: ' + Fore.BLUE + Style.BRIGHT + f'Program Name --> {line.strip()}' + Style.RESET_ALL)
    elif line[0] == '(':
      print(f'{l}: ' + Fore.MAGENTA + Style.DIM + f'==={line.strip()}===' + Style.RESET_ALL)
    elif line[0] == 'M':
      m = lst[0] + str(lst[1].strip())
      print(f'{l}: ' + Fore.RED + f'!!! {get_mcode(m)} !!!' + Style.RESET_ALL)
    else:
      for i in range(len(lst)):
        if type(lst[i]) == int or type(lst[i]) == float:
          pass
        elif lst[i] == 'G':
          g = lst[i] + str(lst[i+1])
          if lst[i+1] == '0':
              rapid = 'ON'
        elif lst[i] == 'X':
          xcom = (f'X={lst[i+1].strip()}')
          if rapid == 'ON':
            print(lst[i+1].strip())
            Rx=lst[i+1].strip()
          else:
            Lx=lst[i+1].strip()
        elif lst[i] == 'Z':
          zcom = (f'Z={lst[i+1].strip()}')
          if rapid == 'ON':
            Rz=lst[i+1].strip()
          else:
            Lz=lst[i+1].strip()
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
  
        linDic.update({l: [float(Lz) if Lz != '' else 0,float(Lx) if Lx != '' else 0]})
        rapDic.update({l: [float(Rz) if Rz != '' else 0, float(Rx) if Rx != '' else 0]})
        cmd = [xcom,zcom]
  
  #=====PRINT OPERATION=========== 
      printcoor = ''
      if 'X' in line:
        printcoor = color.GREEN + 'Travel to: ' + color.END + xcom
      elif 'Z' in line: 
        printcoor = color.GREEN + 'Travel to: ' + color.END + zcom
      if 'X' in line and 'Z' in line:
        printcoor = color.GREEN + 'Travel to: ' + color.END + xcom + ", " + zcom
        
      print(f"{l}: {get_gcode(g) + ' ' if g != '' else ''}{tool if 'T' in line else ''}{speed if 'S' in line else ''}{printcoor}{feed if 'F' in line else ''}{'  --> ' + get_mcode(m)  if m != '' else ''}" + f'_____Tool Position: {xcom},{zcom}' + '\n')
  #=========================
  
  #=====Plot
  linearTrav = list(linDic.items())
  
  for i in range(len(linearTrav)-1,-1,-1):
    if linearTrav[i][1][0] == linearTrav[i-1][1][0] and linearTrav[i][1][1] == linearTrav[i-1][1][1]:
      linearTrav.pop(i-1)
  for i in range(len(linearTrav)-1,-1,-1):
    if linearTrav[i][1][0] == linearTrav[i-1][1][0] and linearTrav[i][1][1] == linearTrav[i-1][1][1]:
      linearTrav.pop(i-1)
  
  rapidTrav = list(rapDic.items())  #Separate Rapid paths from Cutting paths
  
  for i in range(len(rapidTrav)-1,-1,-1):
    if rapidTrav[i][1][0] == rapidTrav[i-1][1][0] and rapidTrav[i][1][1] == rapidTrav[i-1][1][1]:
      rapidTrav.pop(i-1)
  for i in range(len(rapidTrav)-1,-1,-1):
    if rapidTrav[i][1][0] == rapidTrav[i-1][1][0] and rapidTrav[i][1][1] == rapidTrav[i-1][1][1]:
      rapidTrav.pop(i-1)
      
  linx = [i[1][0] for i in linearTrav]
  liny = [i[1][1] for i in linearTrav]
  rapx = [i[1][0] for i in rapidTrav]
  rapy = [i[1][1] for i in rapidTrav]
  
  plt.plot(linx,liny, color='black') #Cutting paths are black
  plt.plot(rapx,rapy, color='red')  #Rapid paths are red
  plt.title("Tool Paths")
  plt.xlabel("z")
  plt.ylabel('x')
  plt.show()
