import tkinter as tk
from PIL import Image, ImageTk




#ventana principal
ventanap1 = tk.Tk()
ventanap1.title("¿PRODUCTOS?")
ventanap1.geometry(f"1024x650")
ventanap1.resizable(False, False)
ventanap1.config(bg="black")


#titulo principal
titulo = tk.Label(ventanap1,
                    text="I DON'T KNOW, BRO", 
                    font=("Cooper Black", 30), background="black", 
                    foreground="white")
titulo.place(x = 290, y = 20)

im = "R.png"

#frames
fr1 = tk.Frame(ventanap1, bg="white")
fr1.place(x=35, y=100, width=300, height=250)

fr2 = tk.Frame(ventanap1, bg="white")
fr2.place(x=380, y=100, width=600, height=250)

fr3 = tk.Frame(ventanap1, bg="white")
fr3.place(x=35, y=380, width=950, height=240)


#titulos y estructura frame 2
titulop = tk.Label(fr2, text="Titulo del producto que quieres comprar", font=("Cooper Black", 20), foreground="black", bg="white").place(x=10, y=5)
titulo_cantidad = tk.Label(fr2, text="cantidad", font=("Cooper Black", 17), foreground="black", bg="white").place(x=20, y=190)
txtprecio = tk.Label(fr2, text="precio: ",  font=("Cooper Black", 19), foreground="black", bg="white").place(x=20, y=120)
precio = tk.Label(fr2, text="50.000",  font=("Cooper Black", 23), foreground="black", bg="white").place(x=120, y=116)


#titulos y estructura frame 3
c1 = tk.Label(fr3, text="1 cosa que te interesa", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=5)
c2 = tk.Label(fr3, text="2 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=30)
c3 = tk.Label(fr3, text="3 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=55)
c4 = tk.Label(fr3, text="4 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=80)
c5 = tk.Label(fr3, text="5 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=105)
c6 = tk.Label(fr3, text="6 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=130)
c7 = tk.Label(fr3, text="7 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=155)
c8 = tk.Label(fr3, text="8 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=180)
c9 = tk.Label(fr3, text="9 cosas que te interesan", font=("Cooper Black", 12), foreground="black", bg="white").place(x=10, y=205)







#botones
botoncomprar = tk.Button(fr2, text="Comprar", font=("Cooper Black", 17), foreground="black", bg="white", border=2).place(x=450, y=180)
boton_cantidad = tk.Spinbox(fr2, font=("Cooper Black", 14), foreground="black", bg="white",width=3).place(x=130, y=195)

ventanap1.mainloop()