from sec import *

def menu_principal():
    while True:
        print("MENU PRINCIPAL")
        print("1. Personas")
        print("2. vehiculos")
        print("3. animales")
        print("4. comidas")
        print("5. salones")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            p = persona()
            print(p.menupersona())
        elif opcion == "2":
            p = vehiculos()
            print(p.menuvehiculos()) 
        elif opcion == "3":
            p = animales()
            print(p.menuanimales())  
        elif opcion == "4":
            p = comidas()
            print(p.menucomidas()) 
        elif opcion == "5":
            p = salones()
            print(p.menusalones())          
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


# Ejecutar el menú principal
menu_principal()