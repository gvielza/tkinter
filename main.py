import tkinter as tk
def mostrar_nombre():
    nombre=entrada.get()
    etiqueta.config(text=f"Hola ,{nombre}")

root=tk.Tk()
root.geometry("300x200")
root.title("mi primera interfaz en python")
etiqueta=tk.Label(root,text="Ingresa tu nombre:")
etiqueta.pack()



entrada=tk.Entry(root)
entrada.pack()

boton=tk.Button(root,text="Saludar", command=mostrar_nombre)
boton.pack()

root.mainloop()