import tkinter as tk 
from PIL import Image, ImageTk


#ventana principal
ventanar = tk.Tk()
pathr = Image.open("registro-img.png")
iconor = ImageTk.PhotoImage(pathr)
ventanar.iconphoto(True, iconor)
ventanar.title("Registro de Usuario") 
ventanar.geometry(f"1024x650")
ventanar.resizable(False, False) 
ventanar.config(bg="black")






#titulos guias
titulo_registror = tk.Label(ventanar, 
                           text="REGISTRO DE USUARIO", 
                           font=("Cooper Black", 30), background="black", 
                           foreground="white")
titulo_registror.place(x = 400, y = 170, height=28)

nombrer = tk.Label(ventanar, 
                  text="Ingrese su nombre", 
                  font=("Cooper Black", 15), 
                  background="black", 
                  foreground="white")
nombrer. place(x = 400, y = 216)

apellidor = tk.Label(ventanar, 
                    text="Ingrese su apellido", 
                    font=("Cooper Black", 15), 
                    background="black", 
                    foreground="white")
apellidor.place(x = 400, y = 275)

correor = tk.Label(ventanar, 
                  text="Ingrese su correo", 
                  font=("Cooper Black", 15), 
                  background="black", 
                  foreground="white")
correor.place(x = 400, y = 335)

nombre_de_usuarior = tk.Label(ventanar, 
                             text="Ingrese su nombre de usuario", 
                             font=("Cooper Black", 15), 
                             background="black", 
                             foreground="white")
nombre_de_usuarior.place(x = 400, y = 396)

claver = tk.Label(ventanar, 
                 text="Ingrese su contraseña a usar", 
                 font=("Cooper Black", 15), 
                 background="black", 
                 foreground="white")
claver.place(x = 400, y = 456)




#ingreso de datos por el usuario


nombre1r = tk.Entry(ventanar, width=25, font=20, bg="black", foreground="white", border=0)
nombre1r.place(x = 400, y = 244, height=22)
apellido1r = tk.Entry(ventanar, width=25, font=20, bg="black", foreground="white", border=0)
apellido1r.place(x = 400, y = 303, height=22)
correo1r = tk.Entry(ventanar, width=35, font=20, bg="black", foreground="white", border=0)
correo1r.place(x = 400, y = 363, height=22)
nombre_de_usuario1r = tk.Entry(ventanar, width=25, font=20, bg="black", foreground="white", border=0)
nombre_de_usuario1r.place(x = 400, y = 424, height=22)
clave1r = tk.Entry(ventanar, width=30, font=20, bg="black", foreground="white", border=0)
clave1r.place(x = 400, y = 484, height=22)


tk.Frame(ventanar, width=320, height=2, bg="white").place(x=400, y=265)
tk.Frame(ventanar, width=320, height=2, bg="white").place(x=400, y=325)
tk.Frame(ventanar, width=320, height=2, bg="white").place(x=400, y=384)
tk.Frame(ventanar, width=320, height=2, bg="white").place(x=400, y=445)
tk.Frame(ventanar, width=320, height=2, bg="white").place(x=400, y=505)



#enviar a base de datos

def registro():
    nombre2 = nombre1r.get()
    apellido2 = apellido1r.get()
    correo2 = correo1r.get()
    nombre_de_usuario2 = nombre_de_usuario1r.get()
    clave2 = clave1r.get()

botonr = tk.Button(ventanar, text = "Registrarse", command = registro, font=("Cooper Black", 18), border=5)
botonr.place(x = 555, y = 550) 



frame_logor = tk.Frame(ventanar, bd=0, width=300, relief=tk.SOLID, padx=0, pady=0, bg="black")
frame_logor.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
labelr = tk.Label(frame_logor, image=iconor, bg="#F4F5F7")
labelr.place(x=0, y=0, relwidth=1, relheight=1)




ventanar.mainloop()