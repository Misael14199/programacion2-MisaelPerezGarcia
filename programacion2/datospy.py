class persona:
    
    def __init__(self,nombre,apellido,correo,telefono,cedula):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.telefono=telefono
        self.cedula=cedula
        
    def obtenernombre(self):
        return f'mi nombre es {self.nombre} {self.apellido} {self.cedula} {self.correo} {self.telefono}'
        
p=persona("misael","perez,","10471661,","misaelperez18@gmail.com","3104844552,")
print(p.obtenernombre())