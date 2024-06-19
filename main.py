# Práctica Lista Simple iniciada en la clase 3 y continuada en clase 4

from ListaEnlazada import ListaEnlazada
miLista = ListaEnlazada()
numero = 0
opcion = 0

def intinput(string):
    bandera = False
    while not bandera:
        try:
            entero = int(input(string))
            bandera = True
        except ValueError:
            print("No es un entero válido")
    return entero

while opcion !=8:
    opcion= intinput("Digite la opcion que requiera: \n"
                      "1. Ingresar \n"
                      "2. Mostrar \n"
                      "3. Buscar \n"
                      "4. Modificar \n"
                      "5. Eliminar \n"
                      "6. Ordenar ascendente\n"
                      "7. Ordenar descendente\n"
                      "8. Salir \n: ")
    match opcion:
        case 1:
            numero= intinput("Digite el número que desea insertar: ")
            miLista.insertarNodo(numero)
        case 2:
            print(miLista.mostrarLista())
        case 3:
            numero=intinput("Digite el número que desea buscar: ")
            if miLista.buscarNodo(numero):
                print("El número se encuentra en la lista")
            else:
                print("El número NO se encuentra en la lista")
        case 4:
            datoActual=intinput("Digite el número que desea modificar: ")
            datoNuevo=intinput("Digite el nuevo número con el que lo desea cambiar: ")
            miLista.modificarNodo(datoActual,datoNuevo)
        case 5:
            numero= int(input("Digite el número que desea eliminar: "))
            miLista.eliminarNodo(numero)
        case 6:
            miLista.ordenar_ascendente()
        case 7:
            miLista.ordenar_descendente()
        case 8:
            print("Saliendo del programa... ")
        case _:
            print("Opción inválida")