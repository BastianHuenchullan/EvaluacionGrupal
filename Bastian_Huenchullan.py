# Una empresa de transporte PasajeBus necesita un sistema básico que permita vender pasajes de bus numerados. Cada pasaje corresponde a un asiento único.
# El sistema debe mantener una lista de los asientos disponibles, y cuando un pasajero compra, ese asiento se elimina de la lista.


asientos_disponibles = [1, 2, 3, 4, 5]
asientos_registrados = {}

while True:
    try:
        opcion = int(input("""
***** SISTEMA DE PASAJES PASAJEBUS *****

1.- Ver asientos disponibles
2.- Comprar pasaje
3.- Ver pasajeros registrados
4.- Salir

Seleccione una opción: """))
    except ValueError:
        print("- Error: Ingresa un número, por favor.")
        continue

    if opcion == 1:
        print("- Asientos disponibles: " + ", ".join(str(asiento) for asiento in asientos_disponibles))

    elif opcion == 2:
        
        rut = input("Ingrese su RUT: ").replace(" ", "").replace("-", "").replace(".", "").upper()

        if (rut[-1].isdigit() or rut[-1] == "K") and rut[:-1].isdigit():
            rut_formateado = rut[:-1] + "-" + rut[-1]
        else:
            print("- RUT Inválido.")
            continue

        try:
            opcion_compra = int(input("Ingrese número de asiento a comprar: "))
        except ValueError:
            print("- Error: Ingresa un número, por favor.")
            continue

        if opcion_compra in asientos_disponibles:
            print(f"- Asiento {opcion_compra} comprado con éxito para el RUT {rut_formateado}.")
            asientos_disponibles.remove(opcion_compra)
            asientos_registrados.update({rut_formateado: opcion_compra})
        else:
            if opcion_compra in (1, 2, 3, 4, 5):
                print("- Lo sentimos, ese asiento ya no está disponible. Prueba con otro.")
            else:
                print("- Elige un asiento válido.")

    elif opcion == 3:
        print("--- Lista de pasajeros ---")
        if asientos_registrados:
            for rut, asiento in asientos_registrados.items():
                print(f"- RUT: {rut}, Asiento: {asiento}")
        else:
            print("- No hay ningún pasajero ni asientos reservados aún.")

    elif opcion == 4:
        print("- ¡Hasta luego! Vuelva pronto.")
        break

    else:
        print("- Opción incorrecta. Por favor, seleccione una opción entre 1-4.")
