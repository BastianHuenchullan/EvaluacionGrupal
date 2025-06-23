asientos_vina = list(range(1, 11))
asientos_valpo = list(range(1, 11))

pasajeros_vina = {}
pasajeros_valpo = {}

def mostrar_menu():
    print("\n***** SISTEMA DE PASAJES PASAJEBUS *****")
    print("1.- Comprar pasaje a Viña del Mar")
    print("2.- Comprar pasaje a Valparaíso")
    print("3.- Ver asientos disponibles")
    print("4.- Ver lista de pasajeros")
    print("5.- Salir")

def comprar_pasaje(destino):
    if destino == "Viña del Mar":
        asientos = asientos_vina
        pasajeros = pasajeros_vina
    else:
        asientos = asientos_valpo
        pasajeros = pasajeros_valpo

    print(f"Asientos disponibles para {destino}: {asientos}")

    rut = input("Ingrese su RUT: ")

    if rut in pasajeros:
        print("Ya tiene un pasaje registrado para este destino.")
        return

    nombre = input("Ingrese su nombre: ")

    try:
        asiento = int(input("Ingrese el número de asiento que desea: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if asiento not in asientos:
        print("Ese asiento no está disponible.")
    else:
        pasajeros[rut] = {"nombre": nombre, "asiento": asiento}
        asientos.remove(asiento)
        print(f"Pasaje registrado con éxito para {nombre} en asiento {asiento} hacia {destino}.")

def ver_asientos_disponibles():
    print("\nAsientos disponibles:")
    print(f"Viña del Mar: {asientos_vina}")
    print(f"Valparaíso: {asientos_valpo}")

def ver_lista_pasajeros():
    print("\nPasajeros a Viña del Mar:")
    for rut, datos in pasajeros_vina.items():
        print(f"RUT: {rut} | Nombre: {datos['nombre']} | Asiento: {datos['asiento']}")

    print("\nPasajeros a Valparaíso:")
    for rut, datos in pasajeros_valpo.items():
        print(f"RUT: {rut} | Nombre: {datos['nombre']} | Asiento: {datos['asiento']}")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        comprar_pasaje("Viña del Mar")
    elif opcion == "2":
        comprar_pasaje("Valparaíso")
    elif opcion == "3":
        ver_asientos_disponibles()
    elif opcion == "4":
        ver_lista_pasajeros()
    elif opcion == "5":
        print("Gracias por usar PasajeBus.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
