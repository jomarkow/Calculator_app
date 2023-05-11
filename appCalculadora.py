from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from math import sqrt

 
# Configuracion ventana 

ventana = Tk()
ventana.overrideredirect(True)
ventana.geometry("300x380")
#ventana.resizable(0,0)
ventana.title("Calculadora")
#ventana.iconbitmap('Calculadora2.0\calc.ico')


# Display superior

Udisplay = Label(ventana, 
                    text = "",
                    font=("Arial", 14),
                    anchor='e',
                    bg = "white", fg = "black", 
                    pady=5, padx=30)

Udisplay.place(x=0,y=0,width=300, height= 30)

# Display superior

display = Label(ventana, 
                text = "",
                font=("Arial", 24, BOLD), 
                anchor='e',
                bg = "white", fg = "black", 
                pady=5, padx=30)

display.place(x=0,y=30,width=300, height= 100)

fun = ''

# Actualizacion de display
def actD (pulso):
    global fun
    fun = fun + pulso
    display.configure(text=fun)   

# Solucionador de cuentas (se puede hacer en pocas lineas con eval())
def solver(cuenta):
    
    cuenta = cuenta.split(" ")
    
    cuenta = [float(c) if c[-1].isdigit() else c for c in cuenta]
    
    pos = 1
    
    while 'x' in cuenta or '÷' in cuenta:
        
        if cuenta[pos] in ('-','+'): pos = pos + 2
        
        else:
            if 'x' in cuenta[pos]: cuenta[pos-1:pos+2] = [cuenta[pos-1] * cuenta[pos+1]]
            
            elif '÷' in cuenta[pos]:
                
                try: cuenta[pos-1:pos+2] = [cuenta[pos-1] / cuenta[pos+1]]
                
                except: 
                    cuenta = messagebox.showwarning("Error", "No se puede dividir entre 0.")
                    display.configure(text='')
                
    while '+' in cuenta or '-' in cuenta:
        
        pos = 1
        
        if '+' in cuenta[pos]: cuenta[pos-1:pos+2] = [cuenta[pos-1] + cuenta[pos+1]]
            
        elif '-' in cuenta[pos]: cuenta[pos-1:pos+2] = [cuenta[pos-1] - cuenta[pos+1]]
    
                    
    return cuenta[0]
        
# Muestra las soluciones en el display
def printer(res):
     
    global fun
    
    if not res - round(res): display.configure(text=str(int(res)))
        
    else: display.configure(text=str(round(res, 3)))
    
    fun = ''
           
# Funcionalidad de las teclas y funcionamiento de la calculadora                                 
def keyFunc (pulso):
    
    global fun
    
    sD, pD = Udisplay.cget("text"), display.cget("text")
    
    if (pD == '' or pD == '-' or pD == '.') and pulso in ('=','x','+','÷'): pass
        
    elif pulso == '=':
     
        Udisplay.configure(text='')
        printer(solver(sD+pD))
            
    elif pulso == 'C': 
        
        Udisplay.configure(text='')
        display.configure(text='')
        fun = ''
    
    elif pulso == 'x²': printer(float(pD)**2)
        
    elif pulso == '√x': printer(sqrt(float(pD)))
        
    elif pulso == '.' and pD.count('.') == 0: actD(pulso)
            
    elif pulso.isdigit(): actD(pulso)
    
    else :
        
        if pD[-1:] in ('-','.') or pulso == '.':
            pass
        
        elif pulso == '-' and pD == '': actD (pulso)
               
        else:
            Udisplay.configure(text=sD+pD+' '+pulso+' ')
            display.configure(text='')
            fun = '' 
    
# Armado de la GUI del teclado        
def keyboard():
    
    def checker(y,x):
    
        keyFunc(teclas[y][x])
    
    teclas = [['C','x²','√x','÷'],
              ['7','8','9','x'],
              ['4','5','6','-'],
              ['1','2','3','+'],
              ['.','0','=','=']]

    pos = [[None for x in range(4)] for y in range(5)]


    for y in range(5):
        
        for x in range(4):
            
            tecla = Button(ventana, 
                        text = teclas[y][x], 
                        font=("Arial", 14), 
                        bg="#ffe8cd",
                        borderwidth=0,
                        command=lambda y = y, x = x: checker(y,x)) 
            
            if teclas[y][x].isdigit(): tecla.configure(bg="#fff3e0")
                
            if teclas[y][x] == "=": 
                tecla.place(x=150,y=330, width=150, height=50) 
                tecla.configure(bg="#ffcc80")
                
            else: 
                tecla.place(x=x*75,y=130+y*50, width=75, height=50)
                
            pos[y][x] = tecla
            
keyboard()
print("hola")
ventana.mainloop()       