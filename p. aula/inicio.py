import tkinter as tk 
from PIL import Image, ImageTk


#ventana principal
ventanai = tk.Tk()
pathi = Image.open("inicio-img.png")
iconoi = ImageTk.PhotoImage(pathi)
ventanai.iconphoto(True, iconoi)
ventanai.title("INICIO DE SESION") 
ventanai.geometry(f"1024x650")
ventanai.resizable(False, False) 
ventanai.config(bg="black")


#titulos guias
titulo_registroi = tk.Label(ventanai, 
                           text="INICIO DE SESION", 
                           font=50, background="black", 
                           foreground="white")
titulo_registroi.place(x = 400, y = 170, height=25)

nombre_usuarioi = tk.Label(ventanai, 
                  text="Ingrese su nombre de usuario", 
                  font=50, background="black", 
                  foreground="white")
nombre_usuarioi. place(x = 400, y = 216)

clavei = tk.Label(ventanai, 
                    text="Ingrese su contraseña", 
                    font=50, background="black", 
                    foreground="white")
clavei.place(x = 400, y = 275)





#ingreso de datos por el usuario
nombre_usuarioi1 = tk.Entry(ventanai, width=25, font=20)
nombre_usuarioi1.place(x = 400, y = 240, height=22)
clavei1 = tk.Entry(ventanai, width=25)
clavei1.place(x = 400, y = 299, height=22)



#comprobacion de datos

def inicio():
    nombre_usuarioi2 = nombre_usuarioi1.get()
    clavei2 = clavei1.get()

botoni = tk.Button(ventanai, text = "Iniciar Sesion", command = inicio, font=30, borderwidth=5)
botoni.place(x = 445, y = 350) 


frame_logoi = tk.Frame(ventanai, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="#F4F5F7")
frame_logoi.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
labeli = tk.Label(frame_logoi, image=pathi, bg="#F4F5F7")
labeli.place(x=0, y=0, relwidth=1, relheight=1)


ventanai.mainloop()