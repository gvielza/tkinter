import tkinter as tk
import subprocess
def mostrar_nombre():
    nombre=entrada.get()
    etiqueta.config(text=f"Hola ,{nombre}")

def metodo_propina():
    root.destroy()
    subprocess.run(['python',"calculadora_propinas.py"])

def def_formulario():
    root.destroy()
    subprocess.run(['python','form.py'])

root=tk.Tk()
root.geometry("300x200")
root.title("mi primera interfaz en python")
etiqueta=tk.Label(root,text="Ingresa tu nombre:")
etiqueta.pack()



entrada=tk.Entry(root)
entrada.pack()

boton=tk.Button(root,text="Saludar", command=mostrar_nombre)
boton.pack()

boton_link=tk.Button(root,text="Calculadora de Propinas", command=metodo_propina)
boton_link.pack()

boton_formulario=tk.Button(text="Ingresar Datos", command=def_formulario)
boton_formulario.pack()

root.mainloop()