from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("formulario en tkinter | andres")

# texto encabezado
encabezado = Label(ventana, text="formularios con tkinter - 44ndres")
encabezado.config(
   fg="white",
   bg="darkgray",
   font=("open sans", 18),  
   padx=10,
   pady=10
)
encabezado.pack() 

ventana.mainloop()