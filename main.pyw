from tkinter import Tk, Frame, Entry, Button, END

i = 0


def insetar(valor):
    global i
    entrada.insert(i, valor)
    i += 1


def borrar():
    global i
    entrada.delete(0, END)
    i = 0


def operar():
    global i
    contenido = entrada.get()
    operacion = eval(contenido)
    entrada.delete(0, END)
    entrada.insert(i, operacion)
    i += 1
    pass


ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("300x240")
ventana.resizable(False, False)

frame = Frame(ventana, background='black')
frame.place(x=0, y=0, width=300, height=240)

entrada = Entry(frame, justify="right", font=("Arial", 16, "bold"), borderwidth=3, bg="#A8DF8E")
entrada.place(x=0, y=0, width=300, height=40)

# botones de numeros2
boton1 = Button(frame, text="1", font=("Arial", 14, "bold"), command=lambda: insetar(1), bg="#EBE76C")
boton2 = Button(frame, text="2", font=("Arial", 14, "bold"), command=lambda: insetar(2), bg="#EBE76C")
boton3 = Button(frame, text="3", font=("Arial", 14, "bold"), command=lambda: insetar(3), bg="#EBE76C")
boton4 = Button(frame, text="4", font=("Arial", 14, "bold"), command=lambda: insetar(4), bg="#EBE76C")
boton5 = Button(frame, text="5", font=("Arial", 14, "bold"), command=lambda: insetar(5), bg="#EBE76C")
boton6 = Button(frame, text="6", font=("Arial", 14, "bold"), command=lambda: insetar(6), bg="#EBE76C")
boton7 = Button(frame, text="7", font=("Arial", 14, "bold"), command=lambda: insetar(7), bg="#EBE76C")
boton8 = Button(frame, text="8", font=("Arial", 14, "bold"), command=lambda: insetar(8), bg="#EBE76C")
boton9 = Button(frame, text="9", font=("Arial", 14, "bold"), command=lambda: insetar(9), bg="#EBE76C")
boton0 = Button(frame, text="0", font=("Arial", 14, "bold"), command=lambda: insetar(0), bg="#EBE76C")

# botones operadores

boton_suma = Button(frame, text="+", font=("Arial", 14, "bold"), command=lambda: insetar("+"), bg="#40F8FF")
boton_resta = Button(frame, text="-", font=("Arial", 14, "bold"), command=lambda: insetar("-"), bg="#40F8FF")
boton_abreparentesis = Button(frame, text="(", font=("Arial", 14, "bold"), command=lambda: insetar("("), bg="#40F8FF")
boton_cierraparentesis = Button(frame, text=")", font=("Arial", 14, "bold"), command=lambda: insetar(")"), bg="#40F8FF")
boton_multiplicacion = Button(frame, text="x", font=("Arial", 14, "bold"), command=lambda: insetar("*"), bg="#40F8FF")
boton_division = Button(frame, text="/", font=("Arial", 14, "bold"), command=lambda: insetar("/"), bg="#40F8FF")
boton_igual = Button(frame, text="=", font=("Arial", 14, "bold"), command=operar, bg="#40F8FF")
boton_decimal = Button(frame, text=".", font=("Arial", 14, "bold"), command=lambda: insetar("."), bg="#40F8FF")
boton_borrar = Button(frame, text="AC", font=("Arial", 14, "bold"), command=borrar, bg="#40F8FF")

# ubicaciones

boton_borrar.place(x=0, y=40, width=75, height=40)
boton_abreparentesis.place(x=75, y=40, width=75, height=40)
boton_cierraparentesis.place(x=150, y=40, width=75, height=40)
boton_division.place(x=225, y=40, width=75, height=40)

boton7.place(x=0, y=80, width=75, height=40)
boton8.place(x=75, y=80, width=75, height=40)
boton9.place(x=150, y=80, width=75, height=40)
boton_multiplicacion.place(x=225, y=80, width=75, height=40)

boton4.place(x=0, y=120, width=75, height=40)
boton5.place(x=75, y=120, width=75, height=40)
boton6.place(x=150, y=120, width=75, height=40)
boton_resta.place(x=225, y=120, width=75, height=40)

boton1.place(x=0, y=160, width=75, height=40)
boton2.place(x=75, y=160, width=75, height=40)
boton3.place(x=150, y=160, width=75, height=40)
boton_suma.place(x=225, y=160, width=75, height=80)

boton0.place(x=0, y=200, width=75, height=40)
boton_decimal.place(x=75, y=200, width=75, height=40)
boton_igual.place(x=150, y=200, width=75, height=40)

ventana.mainloop()
