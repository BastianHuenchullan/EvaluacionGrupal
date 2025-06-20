def errores(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Ingrese solo numeros")

def menu():
    print("*"*5, "SISTEMA DE PASAJEBUS", "*"*5)
    return ("1.- Ver asientos disponibles\n2.- Comprar pasaje\n3.- Ver pasajeros\n4.- Salir\nSeleccione una opción: ")

asientos = list(range(1,11))
pasajeros = {}

while True:
    user = errores(menu())
    if user == 1:
       print(f"Asientos disponibles {asientos}")
    elif user == 2:
        if not asientos:
            print("No hay asientos disponibles")
            continue
        rut = errores("Ingrese su RUT (sin puntos ni guion): ")
        rut = str(rut)
        if len(rut) < (9):
            print("Ingrese un RUT valido")
            continue
        if rut in pasajeros:
            print("El rut ya esta registrado o es invalido")
            continue
        comprar = errores("Ingrese el numero del asiento a comprar: ")
        if comprar not in asientos:
            print("El asiento no esta disponible o es invalido ")
            continue
        asientos.remove(comprar)
        pasajeros[rut] = comprar
        print(f"Compro el asiento numero {comprar}")
    elif user == 3:
        if not pasajeros:
            print("Todabia no hay pasajeros")
            
        else:
            for i, j in pasajeros.items():
                print(f"Pasajero {i} -> Asiento: {j}")
    elif user == 4:
        print("Gracias por comprar con PasajeBus\nSaliendo...")
        break
    else:
        print("Ingresa una opcion valida (1-4)")