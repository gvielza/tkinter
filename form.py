import tkinter as tk

form=tk.Tk()
form.config(background="#123456")
form.geometry("300x300")
form.title("Formulario de Registro")

# Etiquetas
tk.Label(form, text="Nombre:",width=18).grid(row=0, column=0, padx=10, pady=10)
tk.Label(form, text="Apellido:",width=18).grid(row=1, column=0, padx=10, pady=10)
tk.Label(form, text="Correo Electrónico:",width=18).grid(row=2, column=0, padx=10, pady=10)
tk.Label(form, text="Contraseña:",width=18).grid(row=3, column=0, padx=10, pady=10)

# Entradas
entry_nombre = tk.Entry(form)
entry_apellido = tk.Entry(form)
entry_email = tk.Entry(form)
entry_password = tk.Entry(form, show="*")

entry_nombre.grid(row=0, column=1, padx=10, pady=10)
entry_apellido.grid(row=1, column=1, padx=10, pady=10)
entry_email.grid(row=2, column=1, padx=10, pady=10)
entry_password.grid(row=3, column=1, padx=10, pady=10)

# Botón
submit_button = tk.Button(form, text="Enviar")
submit_button.grid(row=4, column=0, columnspan=2, pady=10)



tk.mainloop()