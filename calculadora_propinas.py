'''Debes crear una aplicación tkinter simple que funcione como una calculadora de propinas. La aplicación debe tener una interfaz con un campo de entrada para el 
monto de la cuenta y botones para calcular la propina. Debes usar etiquetas para mostrar los resultados.
'''
import tkinter as tk

def calcular_propina():
    total=float(entrada_total.get())
    porcentaje=float(entrada_porcentaje.get())/100
    propina=total*porcentaje
    resultado_var.set(f"Propina: ${propina:.2f}")

ventana=tk.Tk()
ventana.title("Calculadora de propinas")
ventana.geometry("300x200")
ventana.config(bg="cyan")

label_total=tk.Label(ventana, text="Total: ")
label_total.config(bg="cyan")
label_total.pack()
entrada_total=tk.Entry(ventana)
entrada_total.pack()

label_pp=tk.Label(ventana, text="Porcentaje de Propina")
label_pp.config(bg="cyan")
label_pp.pack()
entrada_porcentaje=tk.Entry(ventana)
entrada_porcentaje.pack()

resultado_var=tk.StringVar()
label_resultado=tk.Label(ventana,textvariable=resultado_var)
label_resultado.config(bg="cyan")
label_resultado.pack()

boton=tk.Button(ventana,text="Calcular", command=calcular_propina,font=("Arial", 12, "bold"), relief="raised")
#boton.config(border="2")
boton.pack()

ventana.mainloop()