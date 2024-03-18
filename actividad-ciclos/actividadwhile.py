x14=True
def menu():
        print("1. persona")
        print("2. vehiculos")
        print("3. universidades")
        print("4. notas")
        print("5. salir")
while(x14):
       menu()
   
       x=int(input("Seleccione su opcion de preferencia"))
       if(x==1):
        print("usted a seleccionado la opcion 'persona'")
        
       if(x==2):
        print("usted a seleccionado la opcion 'vehiculos'")
        
       if(x==3):
        print("usted a seleccionado la opcion 'universidades'")
        
       if(x==4):
        print("usted a seleccionado la opcion 'notas'")
        
       if(x==5):
        print("usted a seleccionado la opcion 'salir'")
        exit()
        

       if(x<1 or x>5):
        print("dato invalido")          

