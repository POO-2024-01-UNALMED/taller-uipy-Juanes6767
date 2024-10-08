from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=40, padx=1, pady=1)
result=""
def sum():
    result=pantalla.get()+"+"
    pantalla.delete(0,"end")
    pantalla.insert(0,result)
def div():
    result = pantalla.get() + "/"
    pantalla.delete(0, "end")
    pantalla.insert(0, result)
def igu():
    entry=pantalla.get()
    if "+"in entry:
        entry.split("+")
        result=float(entry[0])+float(entry[2])
    elif "-"in entry:
        entry.split("+")
        result=float(entry[0])-float(entry[2])
    elif "*"in entry:
        entry.split("+")
        result=float(entry[0])+float(entry[2])
    elif "/"in entry:
        entry.split("+")
        result=float(entry[0])+float(entry[2])
    pantalla.delete(0, "end")
    pantalla.insert(0, result)
def mul():
    result = pantalla.get() + "*"
    pantalla.delete(0, "end")
    pantalla.insert(0, result)
def dig(text):
    result = pantalla.get() + text
    pantalla.delete(0, "end")
    pantalla.insert(0, result)
def men():
    result = pantalla.get() + "-"
    pantalla.delete(0, "end")
    pantalla.insert(0, result)
def pun():
    result = pantalla.get() + "."
    pantalla.delete(0, "end")
    pantalla.insert(0, result)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:dig("9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",command=igu).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,command=pun).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=sum).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=men).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=mul).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=div).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()