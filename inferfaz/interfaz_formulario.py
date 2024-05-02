import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox

#ventana principal
ventanap = tk.Tk()
#Agregando icono a la ventana
path = Image.open("rayo.png")
icono = ImageTk.PhotoImage(path)
ventanap.iconphoto(True, icono)
# Establecemos el nombre del titulo de la ventana.
ventanap.title("Formulario - Datos de Usuario") 
ventanap.geometry(f"1024x920")
# Definimos si la ventana puede ser modificada en su tamaño.
ventanap.resizable(True, True) 
# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventanap.config(bg="black")

def mostrar():
    nombre_in = nombre1.get()
    apellido_in = apellido1.get()
    edad_in = edad1.get()
    direccion_in = direccion1.get()
    telefono_in = telefono1.get()


    seleccion = variable.get()



    seleccionados = cuadro_ciudades.curselection()
    for index in seleccionados:
        elemento = cuadro_ciudades.get(index)
        

    
    
    
    
    messagebox.showinfo("Datos de Usuario Obtenidos", message = (nombre_in, apellido_in, edad_in, direccion_in, telefono_in, seleccion, elemento))





variable = tk.StringVar()

sexo1 = tk.Radiobutton(ventanap, text="Masculino", variable=variable, value="Masculino")
sexo1.grid(row=15, column=3, sticky="w", pady=10, padx=70)

sexo2 = tk.Radiobutton(ventanap, text="Femenino", variable=variable, value="Femenino")
sexo2.grid(row=16, column=3, sticky="w", pady=10, padx=70)



cuadro_ciudades = tk.Listbox(ventanap, width=12, height=4, selectmode="single")
cuadro_ciudades.grid(row=18, column=3, sticky="w", pady=10, padx=70)

elementos = ["Cartagena", "Barranquilla", "Turbaco", "Sincelejo"]

for elemento in elementos:
    cuadro_ciudades.insert(tk.END, elemento)







titulo = tk.Label(ventanap, text="INGRESE SUS DATOS", padx=4, font=20)
titulo.grid(row=3, column=3, sticky="w", pady=20)

nombre = tk.Label(ventanap, text="Nombre:", padx=4)
nombre.grid(row=5, column=3, sticky="w", pady=10)

apellido = tk.Label(ventanap, text="Apellido:", padx=4)
apellido.grid(row=7, column=3, sticky="w", pady=10)

edad = tk.Label(ventanap, text="Edad:", padx=13)
edad.grid(row=9, column=3, sticky="w", pady=10)

direccion = tk.Label(ventanap, text="Direccion:")
direccion.grid(row=11, column=3, sticky="w", pady=10)

telefono = tk.Label(ventanap, text="Telefono:", padx=3)
telefono.grid(row=13, column=3, sticky="w", pady=10)

genero = tk.Label(ventanap, text="Genero:", padx=7)
genero.grid(row=15, column=3, sticky="w", pady=10)

ciudad = tk.Label(ventanap, text="Ciudad:", padx=7)
ciudad.grid(row=18, column=3, sticky="w", pady=10)





nombre1 = tk.Entry(ventanap, width=20)
nombre1.grid(row=5, column=3, sticky="w", pady=10, padx=70)

apellido1 = tk.Entry(ventanap, width=20)
apellido1.grid(row=7, column=3, sticky="w", pady=10, padx=70)

edad1 = tk.Entry(ventanap, width=20)
edad1.grid(row=9, column=3, sticky="w", pady=10, padx=70)

direccion1 = tk.Entry(ventanap, width=30)
direccion1.grid(row=11, column=3, sticky="w", pady=10, padx=70)

telefono1 = tk.Entry(ventanap, width=20)
telefono1.grid(row=13, column=3, sticky="w", pady=10, padx=70)











boton1 = tk.Button(ventanap, text = "obtener datos", command = mostrar)
boton1.grid(row=20, column = 3)
datos = tk.Label(ventanap, text= "datos ")
datos.grid(row=25, column=3)











ventanap.mainloop()