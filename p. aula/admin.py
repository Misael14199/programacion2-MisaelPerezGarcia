import tkinter as tk 
from PIL import Image, ImageTk




#ventana principal
ventanaa = tk.Tk()
patha = Image.open("admin5.png")
iconoa = ImageTk.PhotoImage(patha)
ventanaa.iconphoto(True, iconoa)
ventanaa.title("Configuraciones de administrador") 
ventanaa.geometry(f"1050x650")
ventanaa.resizable(False, False) 
ventanaa.config(bg="black")

tituloadmin = tk.Label(ventanaa, 
                           text="SESION DE ADMINISTRADOR", 
                           font=("Cooper Black", 30), background="black", 
                           foreground="white")
tituloadmin.place(x = 400, y = 100, height=28)


#funciones de opciones de admin
       
def cerrar():
    ventanaa.destroy()


#botones de accion de admin
botonregistrar = tk.Button(ventanaa, text="Registar Usuario",  font=("Cooper Black", 18), border=5)
botonregistrar.place(x=400, y=200)

botonactualizar = tk.Button(ventanaa, text="Actualizar Usuario",  font=("Cooper Black", 18), border=5)
botonactualizar.place(x=400, y=280)

botonborrar = tk.Button(ventanaa, text="Borrar Usuario",  font=("Cooper Black", 18), border=5)
botonborrar.place(x=400, y=360)

botoncerrar = tk.Button(ventanaa, text = "Cerrar Sesion", command=cerrar, font=("Cooper Black", 18), border=5)
botoncerrar.place(x = 540, y = 500) 



#posicion de la imagen de admin
frame_logor = tk.Frame(ventanaa, bd=0, width=320, relief=tk.SOLID, padx=30, pady=210, bg="black")
frame_logor.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
labelr = tk.Label(frame_logor, image=iconoa, bg="white")
labelr.place(x=50, y=0, relwidth=1, relheight=1)


ventanaa.mainloop()