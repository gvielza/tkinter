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

tk.Label(ventana, text="Total: ").pack()
entrada_total=tk.Entry(ventana)
entrada_total.pack()

tk.Label(ventana, text="Porcentaje de Propina").pack()
entrada_porcentaje=tk.Entry(ventana)
entrada_porcentaje.pack()

resultado_var=tk.StringVar()
tk.Label(ventana,textvariable=resultado_var).pack()

tk.Button(ventana,text="Calcular", command=calcular_propina).pack()

ventana.mainloop()