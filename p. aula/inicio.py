import tkinter as tk 
from PIL import Image, ImageTk


#ventana principal
ventanai = tk.Tk()
pathi = Image.open("inicio-img.png")
iconoi = ImageTk.PhotoImage(pathi)
ventanai.iconphoto(True, iconoi)
ventanai.title("Inicio de sesion") 
ventanai.geometry(f"1024x650")
ventanai.resizable(False, False) 
ventanai.config(bg="black")


#titulos guias
titulo_registror = tk.Label(ventanai, 
                           text="INICIO DE SESION", 
                           font=("Cooper Black", 30), background="black", 
                           foreground="white")
titulo_registror.place(x = 400, y = 100, height=28)

nombre_usuarioi = tk.Label(ventanai, 
                  text="Ingrese su nombre de usuario", 
                  font=("Cooper Black", 15), 
                  background="black", 
                  foreground="white")
nombre_usuarioi. place(x = 400, y = 170)

clavei = tk.Label(ventanai, 
                    text="Ingrese su clave", 
                    font=("Cooper Black", 15), 
                    background="black", 
                    foreground="white")
clavei.place(x = 400, y = 270)





#ingreso de datos por el usuario
nombre_usuarioi1 = tk.Entry(ventanai, width=25, font=20, bg="black", foreground="white", border=0)
nombre_usuarioi1.place(x = 400, y = 200, height=22)
clavei1 = tk.Entry(ventanai, width=25, font=20, bg="black", foreground="white", border=0)
clavei1.place(x = 400, y = 300, height=22)

tk.Frame(ventanai, width=320, height=2, bg="white").place(x=400, y=222)
tk.Frame(ventanai, width=320, height=2, bg="white").place(x=400, y=322)



#comprobacion de datos

def inicio():
    nombre_usuarioi2 = nombre_usuarioi1.get()
    clavei2 = clavei1.get()

botoni = tk.Button(ventanai, text = "Iniciar Sesion", command = inicio, font=("Cooper Black", 18), border=5)
botoni.place(x = 540, y = 370) 


frame_logor = tk.Frame(ventanai, bd=0, width=320, relief=tk.SOLID, padx=30, pady=210, bg="black")
frame_logor.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
labelr = tk.Label(frame_logor, image=iconoi, bg="black")
labelr.place(x=50, y=0, relwidth=1, relheight=1)


ventanai.mainloop()