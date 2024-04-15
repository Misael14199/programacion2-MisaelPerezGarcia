
class persona:
    def __init__(self):
        
        global nombre
        nombre = []
        
        global apellido 
        apellido = []
        
        global cedula 
        cedula = []
        
        global edad 
        edad = []
        
        global genero 
        genero = []



    def menupersona(self):
        while True:
            print("\nMENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(persona.agregar())
            elif opcion == "2":
                print(persona.listar())
            elif opcion == "3":
                print(persona.eliminar())
            elif opcion == "4":
                print(persona.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opcion dentro de los parametros.")
    
    def agregar():
        print(f'SE HA SELECCIONADO LA FUNCION "AGREGAR"')
        nombre1 = input("ingresa el nombre: ")
        apellido2 = input("ingresa el apellido: ")
        cedula3 = input("ingresa el cedula: ")
        edad4 = input("ingresa el edad: ")
        genero5 = input("ingresa el genero: ")

        nombre.append(nombre1)
        apellido.append(apellido2)
        cedula.append(cedula3)
        edad.append(edad4)
        genero.append(genero5)

        

    
    def listar():   
        print(f'SE HA SELECCIONADO LA FUNCION "LISTAR"')
        for i in range(len(nombre)):
            print(i,nombre[i])
        for i in range(len(apellido)):
            print(i,apellido[i])
        for i in range(len(cedula)):
            print(i,cedula[i])
        for i in range(len(edad)):
            print(i,edad[i])
        for i in range(len(genero)):
            print(i,genero[i])
        return nombre, apellido, cedula, edad, genero
    
    
    def eliminar(): 
        print('SE HA SELECCIONADO LA FUNCION "ELIMINAR"')

        referenciap = int(input("Ingrese la referencia del elemento a eliminar: "))
        
        if nombre:

            if 0 <= referenciap < len(nombre):
                eliminadop1 = nombre.pop(referenciap)
                print("el nombre ", eliminadop1, " se elimino")
            

        if apellido:
            
            if 0 <= referenciap < len(apellido):
                eliminadop2 = apellido.pop(referenciap)
                print("el apellido ",eliminadop2, " se elimino")
            

        if cedula:
            
            if 0 <= referenciap < len(cedula):
                eliminadop3 = cedula.pop(referenciap)
                print("la cedula ", eliminadop3, " se elimino")
            
        if edad:
            
            if 0 <= referenciap < len(edad):
                eliminadop4 = edad.pop(referenciap)
                print("la edad ", eliminadop4, " se elimino")

        if genero:
            
            if 0 <= referenciap < len(genero):
                eliminadop5 = genero.pop(referenciap)
                print("el genero ", eliminadop5, " se elimino")       


    def actualizar():
       print('SE HA SELECCIONADO LA FUNCION "ACTUALIZAR"')
       ip = int(input("ingrese el indice a actualizar: "))

       cambiarp1 = input("ingrese el nombre nuevo: ")
       nombre[ip] = cambiarp1
       
       cambiarp2 = input("ingrese el apellido nuevo: ")
       apellido[ip] = cambiarp2

       cambiarp3 = input("ingrese la cedula nueva: ")
       cedula[ip] = cambiarp3

       cambiarp4 = input("ingrese la edad nueva: ")
       edad[ip] = cambiarp4

       cambiarp5 = input("ingrese el genero nuevo: ")
       genero[ip] = cambiarp5            


class vehiculos:     
        def __init__(self):
        
         global tipo
         tipo = []
        
         global nruedas
         nruedas = []
        
         global placa
         placa = []

         global marca
         marca = []
        
         global pais
         pais = []
        
        
        def menuvehiculos(self):
            while True:
                print("\nMENU PERSONAS")
                print("1. Crear")
                print("2. Listar")
                print("3. Eliminar")
                print("4. actualizar")
                print("5. Volver al menú principal")
  
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                 print(vehiculos.agregar())
                elif opcion == "2":
                 print(vehiculos.listar())
                elif opcion == "3":
                 print(vehiculos.eliminar())
                elif opcion == "4":
                 print(vehiculos.actualizar())
                elif opcion == "5":
                 break
                else:
                 print("Opción inválida. Por favor, seleccione una opcion dentro de los parametros.")

        def agregar():
         print(f'SE HA SELECCIONADO LA FUNCION "AGREGAR"')
         tipo1 = input("ingresa el tipo de vehiculo: ")
         nruedas2 = input("ingresa el numero de ruedas: ")
         placa3 = input("ingresa el numero de placa: ")
         marca4 = input("ingresa la marca del vehiculo: ")
         pais5 = input("ingresa el pais en el que se registro: ")

         tipo.append(tipo1)
         nruedas.append(nruedas2)
         placa.append(placa3)
         marca.append(marca4)
         pais.append(pais5)       


        def listar():   
         print(f'SE HA SELECCIONADO LA FUNCION "LISTAR"')
         for i in range(len(tipo)):
            print(i,tipo[i])
         for i in range(len(nruedas)):
            print(i,nruedas[i])
         for i in range(len(placa)):
            print(i,placa[i])
         for i in range(len(marca)):
            print(i,marca[i])
         for i in range(len(pais)):
            print(i,pais[i])
         return tipo, nruedas, placa, marca, pais 
        
        def eliminar(): 
         print('"SE HA SELECCIONADO LA FUNCION "ELIMINAR"')
         referenciav = int(input("Ingrese la referencia del elemento a eliminar: "))
         
         if tipo:

            if 0 <= referenciav < len(tipo):
                eliminadov1 = tipo.pop(referenciav)
                print("el tipo ", eliminadov1, " se elimino")
            

         if nruedas:
            
            if 0 <= referenciav < len(nruedas):
                eliminadov2 = nruedas.pop(referenciav)
                print("el numero de ruedas ",eliminadov2, " se elimino")
            

         if placa:
            
            if 0 <= referenciav < len(placa):
                eliminadov3 = placa.pop(referenciav)
                print("la placa ", eliminadov3, " se elimino")
            
         if marca:
            
            if 0 <= referenciav < len(marca):
                eliminadov4 = marca.pop(referenciav)
                print("la marca ", eliminadov4, " se elimino")

         if pais:
            
            if 0 <= referenciav < len(pais):
                eliminadov5 = pais.pop(referenciav)
                print("el pais ", eliminadov5, " se elimino") 

        def actualizar():
         print('SE HA SELECCIONADO LA FUNCION "ACTUALIZAR"')
         iv = int(input("ingrese el indice a actualizar: "))

         cambiarv1 = input("ingrese el tipo de vehiculo nuevo: ")
         tipo[iv] = cambiarv1
       
         cambiarv2 = input("ingrese el numero de ruedas nuevo: ")
         nruedas[iv] = cambiarv2

         cambiarv3 = input("ingrese la placa nueva: ")
         placa[iv] = cambiarv3

         cambiarv4 = input("ingrese la marca nueva: ")
         marca[iv] = cambiarv4

         cambiarv5 = input("ingrese el pais de registro nuevo: ")
         pais[iv] = cambiarv5                



class animales:
     def __init__(self):
        
         global tipoa
         tipoa = []
        
         global npatas
         npatas = []
        
         global transporte
         transporte = []

         global habitad
         habitad = []
        
         global hogar
         hogar = []  


     def menuanimales(self):
            while True:
                print("\nMENU PERSONAS")
                print("1. Crear")
                print("2. Listar")
                print("3. Eliminar")
                print("4. actualizar")
                print("5. Volver al menú principal")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                 print(animales.agregar())
                elif opcion == "2":
                 print(animales.listar())
                elif opcion == "3":
                 print(animales.eliminar())
                elif opcion == "4":
                 print(animales.actualizar())   
                elif opcion == "5":
                 break
                else:
                 print("Opción inválida. Por favor, seleccione una opcion dentro de los parametros.")   

     def agregar():
         print(f'SE HA SELECCIONADO LA FUNCION "AGREGAR"')
         tipoa1 = input("ingresa el tipo de animal: ")
         npatas2 = input("ingresa el numero de patas: ")
         transporte3 = input("ingresa cual es la forma de transportarse: ")
         habitad4 = input("ingresa su habitad: ")
         hogar5 = input("ingresa el pais nativo: ")

         tipoa.append(tipoa1)
         npatas.append(npatas2)
         transporte.append(transporte3)
         habitad.append(habitad4)
         hogar.append(hogar5)       


     def listar():   
         print(f'SE HA SELECCIONADO LA FUNCION "LISTAR"')
         for i in range(len(tipoa)):
            print(i,tipoa[i])
         for i in range(len(npatas)):
            print(i,npatas[i])
         for i in range(len(transporte)):
            print(i,transporte[i])
         for i in range(len(habitad)):
            print(i,habitad[i])
         for i in range(len(hogar)):
            print(i,hogar[i])
         return tipoa, npatas, transporte, habitad, hogar 

     def eliminar(): 
         print('"SE HA SELECCIONADO LA FUNCION "ELIMINAR"')
         referenciaa = int(input("Ingrese la referencia del elemento a eliminar: "))
         
         if tipoa:

            if 0 <= referenciaa < len(tipoa):
                eliminadoa1 = tipoa.pop(referenciaa)
                print("el tipo de animal ", eliminadoa1, " se elimino")
            

         if npatas:
            
            if 0 <= referenciaa < len(npatas):
                eliminadoa2 = npatas.pop(referenciaa)
                print("el numero de patas ",eliminadoa2, " se elimino")
            

         if transporte:
            
            if 0 <= referenciaa < len(transporte):
                eliminadoa3 = transporte.pop(referenciaa)
                print("la forma de transportarse ", eliminadoa3, " se elimino")
            
         if habitad:
            
            if 0 <= referenciaa < len(habitad):
                eliminadoa4 = habitad.pop(referenciaa)
                print("el habitad ", eliminadoa4, " se elimino")

         if hogar:
            
            if 0 <= referenciaa < len(hogar):
                eliminadoa5 = hogar.pop(referenciaa)
                print("el pais de origen  ", eliminadoa5, " se elimino")


     def actualizar():
         print('SE HA SELECCIONADO LA FUNCION "ACTUALIZAR"')
         ia = int(input("ingrese el indice a actualizar: "))

         cambiara1 = input("ingrese el tipo de animal nuevo: ")
         tipoa[ia] = cambiara1
       
         cambiara2 = input("ingrese el numero de patas nuevo: ")
         npatas[ia] = cambiara2

         cambiara3 = input("ingrese la forma de transporte: ")
         transporte[ia] = cambiara3

         cambiara4 = input("ingrese la habitad natural: ")
         habitad[ia] = cambiara4

         cambiara5 = input("ingrese el pais de origen: ")
         hogar[ia] = cambiara5              



class comidas:
   def __init__(self):
        
        global nombrec
        nombrec = []
        
        global ing1
        ing1 = []
        
        global ing2
        ing2 = []

        global ing3
        ing3 = []
        
        global ing4
        ing4 = []  

   def menucomidas(self):
            while True:
                print("\nMENU PERSONAS")
                print("1. Crear")
                print("2. Listar")
                print("3. Eliminar")
                print("4. actualizar")
                print("5. Volver al menú principal")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                 print(comidas.agregar())
                elif opcion == "2":
                 print(comidas.listar())
                elif opcion == "3":
                 print(comidas.eliminar())
                elif opcion == "4":
                   print(comidas.actualizar()) 
                elif opcion == "5":
                 break
                else:
                 print("Opción inválida. Por favor, seleccione una opcion dentro de los parametros.")    

   def agregar():
         print(f'SE HA SELECCIONADO LA FUNCION "AGREGAR"')
         nombrec1 = input("ingresa el nombre de la comida: ")
         print("ingresa 4 ingredientes principales")
         ing11 = input("ingresa el ingrediente #1: ")
         ing22 = input("ingresa el ingrediente #2: ")
         ing33 = input("ingresa el ingrediente #3: ")
         ing44 = input("ingresa el ingrediente #4: ")

         nombrec.append(nombrec1)
         ing1.append(ing11)
         ing2.append(ing22)
         ing3.append(ing33)
         ing4.append(ing44)       


   def listar():   
         print(f'SE HA SELECCIONADO LA FUNCION "LISTAR"')
         for i in range(len(nombrec)):
            print(i,nombrec[i])
         for i in range(len(ing1)):
            print(i,ing1[i])
         for i in range(len(ing2)):
            print(i,ing2[i])
         for i in range(len(ing3)):
            print(i,ing3[i])
         for i in range(len(ing4)):
            print(i,ing4[i])
         return nombrec, ing1, ing2, ing3, ing4  

   def eliminar(): 
         print('"SE HA SELECCIONADO LA FUNCION "ELIMINAR"')
         referenciac = int(input("Ingrese la referencia del elemento a eliminar: "))
         
         if nombrec:

            if 0 <= referenciac < len(nombrec):
                eliminadoa1 = nombrec.pop(referenciac)
                print("la comida ", eliminadoa1, " se elimino")
            

         if ing1:
            
            if 0 <= referenciac < len(ing1):
                eliminadoa2 = ing1.pop(referenciac)
                print("el ingrediente #1 ",eliminadoa2, " se elimino")
            

         if ing2:
            
            if 0 <= referenciac < len(ing2):
                eliminadoa3 = ing2.pop(referenciac)
                print("el ingrediente #2 ", eliminadoa3, " se elimino")
            
         if ing3:
            
            if 0 <= referenciac < len(ing3):
                eliminadoa4 = ing3.pop(referenciac)
                print("el ingrediente #3 ", eliminadoa4, " se elimino")

         if ing4:
            
            if 0 <= referenciac < len(ing4):
                eliminadoa5 = ing4.pop(referenciac)
                print("el ingrediente #4  ", eliminadoa5, " se elimino") 

   def actualizar():
         print('SE HA SELECCIONADO LA FUNCION "ACTUALIZAR"')
         ic = int(input("ingrese el indice a actualizar: "))

         cambiarc1 = input("ingrese el nombre de la comida nueva: ")
         nombrec[ic] = cambiarc1
       
         cambiarc2 = input("ingrese el ingrediente#1 nuevo: ")
         ing1[ic] = cambiarc2

         cambiarc3 = input("ingrese el ingrediente #2: ")
         ing2[ic] = cambiarc3

         cambiarc4 = input("ingrese el ingrediente #3: ")
         ing3[ic] = cambiarc4

         cambiarc5 = input("ingrese el ingrediente #4: ")
         ing4[ic] = cambiarc5              
                 


class salones:
    def __init__(self):
        
        global curso
        curso = []
        
        global hombres
        hombres = []
        
        global mujeres
        mujeres = []

        global materias
        materias = []
        
        global horario
        horario = []  

    def menusalones(self):
            while True:
                print("\nMENU PERSONAS")
                print("1. Crear")
                print("2. Listar")
                print("3. Eliminar")
                print("4. actualizar")
                print("5. Volver al menú principal")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                 print(salones.agregar())
                elif opcion == "2":
                 print(salones.listar())
                elif opcion == "3":
                 print(salones.eliminar())
                elif opcion == "4":
                 print(salones.actualizar()) 
                elif opcion == "5":
                 break
                else:
                 print("Opción inválida. Por favor, seleccione una opcion dentro de los parametros.")    

    def agregar():
         print(f'SE HA SELECCIONADO LA FUNCION "AGREGAR"')
         curso1 = input("ingresa el curso: ")
         hombres1 = input("ingresa la cantidad de hombres: ")
         mujeres1 = input("ingresa la cantidad de mujeres: ")
         materias1 = input("ingresa el numero de materias dictadas: ")
         horario1 = input("ingresa horario: ")

         curso.append(curso1)
         hombres.append(hombres1)
         mujeres.append(mujeres1)
         materias.append(materias1)
         horario.append(horario1)       


    def listar():   
         print(f'SE HA SELECCIONADO LA FUNCION "LISTAR"')
         for i in range(len(curso)):
            print(i,curso[i])
         for i in range(len(hombres)):
            print(i,hombres[i])
         for i in range(len(mujeres)):
            print(i,mujeres[i])
         for i in range(len(materias)):
            print(i,materias[i])
         for i in range(len(horario)):
            print(i,horario[i])
         return curso, hombres, mujeres, materias, horario 

    def eliminar(): 
         print('"SE HA SELECCIONADO LA FUNCION "ELIMINAR"')
         referenciass = int(input("Ingrese la referencia del elemento a eliminar: "))
         
         if curso:

            if 0 <= referenciass < len(curso):
                eliminados1 = curso.pop(referenciass)
                print("el curso ", eliminados1, " se elimino")
            

         if hombres:
            
            if 0 <= referenciass < len(hombres):
                eliminados2 = hombres.pop(referenciass)
                print("el numero de hombres ",eliminados2, " se elimino")
            

         if mujeres:
            
            if 0 <= referenciass < len(mujeres):
                eliminados3 = mujeres.pop(referenciass)
                print("la numero de mujeres ", eliminados3, " se elimino")
            
         if materias:
            
            if 0 <= referenciass < len(materias):
                eliminados4 = materias.pop(referenciass)
                print("la cantidad de materias ", eliminados4, " se elimino")

         if horario:
            
            if 0 <= referenciass < len(horario):
                eliminados5 = horario.pop(referenciass)
                print("el horario  ", eliminados5, " se elimino")                     


    def actualizar():
        print('SE HA SELECCIONADO LA FUNCION "ACTUALIZAR"')
        icurso = int(input("ingrese el indice a actualizar: "))

        cursos1 = input("ingrese el curso nuevo: ")
        curso[icurso] = cursos1
       
        cambiars2 = input("ingrese la cantidad de hombres nueva: ")
        hombres[icurso] = cambiars2

        cambiars3 = input("ingrese la cantidad de mujeres nuevas: ")
        mujeres[icurso] = cambiars3

        cambiars4 = input("ingrese la cantidad de materias nuevas: ")
        materias[icurso] = cambiars4

        cambiars5 = input("ingrese el horario nuevo: ")
        horario[icurso] = cambiars5       