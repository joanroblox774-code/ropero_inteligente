# -*- coding: utf-8 -*-

import shelve

ARCHIVO = "datos_ropa.dat"

# Datos iniciales
ropa_inicial = [
    {"prenda": "Camisa", "color": "Azul", "talla": "M", "usos": 2},
    {"prenda": "Pantalón", "color": "Verde", "talla": "L", "usos": 43},
    {"prenda": "Zapatos", "color": "Gris", "talla": "42", "usos": 56}
]


def cargar_datos():
    with shelve.open(ARCHIVO) as db:
        if "ropa" not in db:
            db["ropa"] = ropa_inicial
        return db["ropa"]


def guardar_datos(ropa):
    with shelve.open(ARCHIVO) as db:
        db["ropa"] = ropa


def seleccionar_ropa(ropa):
    print("\n--- SELECCIONAR PRENDA ---")

    for i, prenda in enumerate(ropa, start=1):
        print(f"{i}. {prenda['prenda']}")

    try:
        opcion = int(input("Número de prenda: "))

        if 1 <= opcion <= len(ropa):
            ropa[opcion - 1]["usos"] += 1

            print(
                f"Has usado {ropa[opcion - 1]['prenda']}. "
                f"Usos totales: {ropa[opcion - 1]['usos']}"
            )

            guardar_datos(ropa)
        else:
            print("Número no válido.")

    except ValueError:
        print("Debes introducir un número.")


def visualizar_ropa(ropa):
    print("\n--- MI ROPA ---")

    for i, prenda in enumerate(ropa, start=1):
        print(
            f"Prenda {i}: "
            f"{prenda['prenda']}, "
            f"Color: {prenda['color']}, "
            f"Talla: {prenda['talla']}, "
            f"Usos: {prenda['usos']}"
        )


def guardar_ropa(ropa):
    print("\n--- AÑADIR PRENDA ---")

    nombre = input("Nombre de la prenda: ")
    color = input("Color: ")
    talla = input("Talla: ")

    nueva_prenda = {
        "prenda": nombre,
        "color": color,
        "talla": talla,
        "usos": 0
    }

    ropa.append(nueva_prenda)
    guardar_datos(ropa)

    print("Prenda añadida correctamente.")


def eliminar_ropa(ropa):
    print("\n--- ELIMINAR PRENDA ---")

    for i, prenda in enumerate(ropa, start=1):
        print(f"{i}. {prenda['prenda']}")

    try:
        opcion = int(input("Número de prenda a eliminar: "))

        if 1 <= opcion <= len(ropa):
            eliminada = ropa.pop(opcion - 1)
            guardar_datos(ropa)

            print(f"{eliminada['prenda']} eliminada.")
        else:
            print("Número no válido.")

    except ValueError:
        print("Debes introducir un número.")


def visualizar_usos(ropa):
    print("\n--- USOS DE LAS PRENDAS ---")

    for prenda in ropa:
        print(f"{prenda['prenda']}: {prenda['usos']} usos")

def ordena_ropero(misprendas):

    miscamisas = []
    mispantalones = []
    miszapatos = []

    for prenda in misprendas:

        if prenda["tipo"] == "camisa":
            miscamisas.append(prenda)

        elif prenda["tipo"] == "pantalon":
            mispantalones.append(prenda)

        elif prenda["tipo"] == "zapatos":
            miszapatos.append(prenda)

    ropero = [miscamisas, mispantalones, miszapatos]
    

    return ropero

def elegir_conjunto_inteligente(ropa):

    camisas = []
    pantalones = []
    zapatos = []

    for prenda in ropa:

        if prenda["tipo"] == "camisa":
            camisas.append(prenda)

        elif prenda["tipo"] == "pantalon":
            pantalones.append(prenda)

        elif prenda["tipo"] == "zapatos":
            zapatos.append(prenda)

    camisa = min(camisas, key=lambda x: x["usos"])
    pantalon = min(pantalones, key=lambda x: x["usos"])
    zapatos_elegidos = min(zapatos, key=lambda x: x["usos"])

    return camisa, pantalon, zapatos_elegidos


# PROGRAMA PRINCIPAL

ropa = cargar_datos()

while True:

    print("\n------ MI ARMARIO ------")
    print("1 - Seleccionar prenda")
    print("2 - Visualizar ropa")
    print("3 - Añadir prenda")
    print("4 - Eliminar prenda")
    print("5 - Visualizar usos")
    print("6 - Guardar datos")
    print("7 - Ver ropero ordenado")

    print("0 - Salir")

    respuesta = input("Elige una opción: ")

    if respuesta == "1":
        seleccionar_ropa(ropa)

    elif respuesta == "2":
        visualizar_ropa(ropa)

    elif respuesta == "3":
        guardar_ropa(ropa)

    elif respuesta == "4":
        eliminar_ropa(ropa)

    elif respuesta == "5":
        visualizar_usos(ropa)

    elif respuesta == "6":
        guardar_datos(ropa)
        print("Datos guardados correctamente.")
    
    elif respuesta == "7":
        ropero = ordena_ropero(ropa)
        print("\nCAMISAS")
        for prenda in ropero[0]:
          print(prenda["prenda"])

        print("\nPANTALONES")
        for prenda in ropero[1]:
         print(prenda["prenda"])

         print("\nZAPATOS")
         for prenda in ropero[2]:
          print(prenda["prenda"])
    
    elif respuesta == "0":
        print("¡Hasta luego!")
        break
else : print("Opción no válida.")

ropa_inicial = [
    {
        "prenda": "Camisa azul",
        "tipo": "camisa",
        "color": "Azul",
        "talla": "M",
        "usos": 2
    },
    {
        "prenda": "Pantalón verde",
        "tipo": "pantalon",
        "color": "Verde",
        "talla": "L",
        "usos": 43
    },
    {
        "prenda": "Zapatos grises",
        "tipo": "zapatos",
        "color": "Gris",
        "talla": "42",
        "usos": 56
    }
]

