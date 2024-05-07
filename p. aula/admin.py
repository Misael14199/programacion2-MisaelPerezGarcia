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


#titulos guias
titulo_registror = tk.Label(ventanaa, 
                           text="SESION DE ADMINISTRADOR", 
                           font=("Cooper Black", 30), background="black", 
                           foreground="white")
titulo_registror.place(x = 400, y = 100, height=28)

nombre_usuarioi = tk.Label(ventanaa, 
                  text="Ingrese su nombre de usuario", 
                  font=("Cooper Black", 15), 
                  background="black", 
                  foreground="white")
nombre_usuarioi. place(x = 400, y = 170)

clavei = tk.Label(ventanaa, 
                    text="Ingrese su clave", 
                    font=("Cooper Black", 15), 
                    background="black", 
                    foreground="white")
clavei.place(x = 400, y = 270)





#ingreso de datos por el usuario
nombre_usuarioi1 = tk.Entry(ventanaa, width=25, font=20, bg="black", foreground="white", border=0)
nombre_usuarioi1.place(x = 400, y = 200, height=22)
clavei1 = tk.Entry(ventanaa, width=25, font=20, bg="black", foreground="white", border=0)
clavei1.place(x = 400, y = 300, height=22)

tk.Frame(ventanaa, width=320, height=2, bg="white").place(x=400, y=222)
tk.Frame(ventanaa, width=320, height=2, bg="white").place(x=400, y=322)



#comprobacion de datos

def inicio():
    nombre_usuarioi2 = nombre_usuarioi1.get()
    clavei2 = clavei1.get()

botoni = tk.Button(ventanaa, text = "Iniciar Sesion", command = inicio, font=30, borderwidth=5)
botoni.place(x = 540, y = 370) 


frame_logor = tk.Frame(ventanaa, bd=0, width=320, relief=tk.SOLID, padx=30, pady=210, bg="black")
frame_logor.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
labelr = tk.Label(frame_logor, image=iconoa, bg="white")
labelr.place(x=50, y=0, relwidth=1, relheight=1)


ventanaa.mainloop()