#-*- coding: utf-8 -*-#
import shelve

misprendas =[{ "nombre": "Camisa", "color": "Azul", "talla": "M", "usos": 2 },
             { "nombre": "Pantalón", "color": "Verde", "talla": "L", "usos": 43 },
             { "nombre": "Zapatos", "color": "Gris", "talla": "42", "usos": 56 }]
misreglas = {"Camisa":"lavar a mano","Pantalón":
               "Lavar a máquina", "Zapatos":
                 "Limpiar con un paño húmedo"}
config = shelve.open("prendas.dat")

print (config["prendas"] )
print (config["reglas"] )
config["prendas"] = misprendas 
config["reglas"] = misreglas 
config.close()
