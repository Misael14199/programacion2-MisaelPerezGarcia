import tkinter as tk 
from PIL import Image, ImageTk # Requiere instalar Pillow 

ventana = tk.Tk()
#Agregando icono a la ventana
path = Image.open("F-22.jpg")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
# Establecemos el nombre del titulo de la ventana.
ventana.title("Misael Perez") 
ventana.geometry(f"1024x920")
# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 
# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventana.config(bg="black")



#titulo simple
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()


#titulo modificado
etiqueta = tk.Label(ventana, text="BIENVENIDOS", bg="white", fg="black", font=("Arial", 16), width=15, height=2, anchor="center")
etiqueta.pack()


#botones
def cambiar_texto():
    etiqueta.config(text="¡Texto cambiado!")

etiqueta = tk.Label(ventana, text="Texto original")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()


#ingreso de texto
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)
    

etiqueta = tk.Label(ventana, text="Texto ingresado: ")
etiqueta.pack()

cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()



#marcos
# Crear un marco con borde sólido
marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()

# Agregar una etiqueta al marco1
etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()
# Crear un marco con borde en relieve
marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

# Agregar una etiqueta al marco2
etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()



#listado de elementos
def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)


cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()



#casilla con chulo
def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")


variable = tk.IntVar()

casilla_verificacion = tk.Checkbutton(ventana, text="Opción 1", variable=variable, command=obtener_estado)
casilla_verificacion.pack()



#seleccion unica
def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")


variable = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=variable, value=1, command=obtener_seleccion)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="Opción 3", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()




#imagen 1
ventana.geometry("300x200")

label = tk.Label(ventana, text="Ejemplo")
label.place(x=50, y=50)

#boton aceptar
ventana.geometry("300x200")
boton = tk.Button(ventana, text="Aceptar")
boton.place(x=100, y=100, width=100, height=30)


#cuadro de color
ventana.geometry("300x200")
frame = tk.Frame(ventana, bg="purple")
frame.place(x=100, y=200, width=200, height=100)




# Inicializamos la aplicacion
ventana.mainloop()