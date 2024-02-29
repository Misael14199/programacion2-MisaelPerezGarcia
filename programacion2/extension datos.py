from datospy import persona
inicio=True
while inicio:
    inicio2=input("ingrese")
    p=persona("misael","perez,","10471661,","misaelperez18@gmail.com","3104844552,")
    print(p.obtenernombre())
    if inicio2=="fin":
        inicio=False

