vuelo={'aereolinea: ':'avianca',
      'vuelo: ':'av989',
      'origen: ':'ctg',
      'destino: ':'mde',
      'tipomaleta':['cabina','mano','bodega']}

for id,valor, in vuelo.items():
    print(f"{id}:{valor}")
    
print("\nvalores de cada tipo de maleta: ")
for maleta in vuelo["tipomaleta"]:
    print(maleta)    
    