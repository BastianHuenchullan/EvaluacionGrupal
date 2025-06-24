#Ejercicio 2

asientos=[1, 2, 3, 4, 5, 6, 7, 8]
reservados={}

def vericar_error(x, y="ingrese una opción correcta"):
    while True:
        try:
            return int(input(x))
        except ValueError:
            print(y)
def RUT(x):
    while True:
        try:
            rut=int(input(x))
        except ValueError:
            print("Ingreselo en el formato solicitado")
            continue
        rut= str(rut)
        if rut[-1]=="0":
            rut= rut[:-1]+"-"+"K"
        else:
            rut= rut[:-1]+"-"+rut[-1]
        return rut
        


while True:
    print("""
***** SISTEMA DE PASAJES PASAJEBUS *****
1.- Ver asientos disponibles
2.- Comprar pasaje
3.- Ver pasajeros registrados
4.- Salir 
""" )
    selección= vericar_error("Ingrese la opción a realizar: ")
    if selección==1:
        print("Asientos disponibles: ")
        print(*asientos)
    elif selección==2:
        if not asientos:
            print("No hay asientos disponibles, no es posible realizar la compra")
            continue
        rut=RUT("favor, ingresa tu número de RUT sin puntos ni guiones. Si tu RUT termina en la letra k, reemplázala por un  0 : ")

        if rut in reservados:
            print("El RUT ingresado ya cuenta con un  asiento asociado, solo se permite un asiento por pasajero")
        print("Asientos disponibles: ")
        print(*asientos)
        while True:
            asiento=vericar_error("Ingrese el asiento a comprar: ", "Debe seleccionar el asiento a comprar, favor ingresarlo nuevamente")
            if asiento in asientos:
                reservados[rut]= asiento
                asientos.remove(asiento)
                print(f"Felcidades, se realizado la compra exitosamente del pasaje, asiento: {asiento}")
                break
            else:
                print("El asiento a comprar no se encuentra disponible, eliga uno de los siguiemtes: ")
                print(*asientos)
                continue
    elif selección==3:
        if reservados=={}:
            print("No se han realizado registros")
            continue
        else:
            print("Pasajeros registrados: ")
            for x, y in reservados.items():
                print(f"Rut: {x}, asiento: {y}")
    elif selección==4:
        print("Buen viaje")
        break
    else:
        print("opción invalida, favor eligir alguna de las opciones disponible")
        
            
            

            




    