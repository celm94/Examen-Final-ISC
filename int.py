from tkinter import *
principal=Tk()

ancho = 500
alto = 300
titulo = Label(text = 'BIENVENIDOS')
titulo.pack()

principal.geometry(str(ancho)+'x'+str(alto))
principal.title("Examen Final")

nombre = Label(text='Nombre', bg= "#ddd")
nombre.place(x=90, y=50)

apellido = Label(text='Apellido', bg= "#ddd")
apellido.place(x=90, y=80)

dia = Label(text='Día', bg= "#ddd")
dia.place(x=90, y=110)

mes = Label(text='Mes', bg= "#ddd")
mes.place(x=90, y=140)

año = Label(text='Año', bg= "#ddd")
año.place(x=90, y=170)


input1= Entry(principal)
input1.pack()
input1.place(x=160, y=50)

input2= Entry(principal)
input2.pack()
input2.place(x=160, y=80)

input3= Entry(principal)
input3.pack()
input3.place(x=160, y=110)

input4= Entry(principal)
input4.pack()
input4.place(x=160, y=140)

input5= Entry(principal)
input5.pack()
input5.place(x=160, y=170)

btn1 = Button(principal, text ='Función 1')
btn1.pack()
btn1.place(x=65, y=230)

btn2 = Button(principal, text ='Función 2')
btn2.pack()
btn2.place(x=130, y=230)

btn3 = Button(principal, text ='Función 3')
btn3.pack()
btn3.place(x=195, y=230)

btn4 = Button(principal, text ='Función 4')
btn4.pack()
btn4.place(x=260, y=230)

btn5 = Button(principal, text ='Función 5')
btn5.pack()
btn5.place(x=325, y=230)


principal.mainloop()