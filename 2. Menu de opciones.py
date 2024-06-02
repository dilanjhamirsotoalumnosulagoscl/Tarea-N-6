mi_lista = []

while True:
    print("Menú de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista")
    print("3. Eliminar un elemento de la lista")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        mi_lista.append(elemento)
        print("Elemento agregado con éxito!")

    elif opcion == "2":
        numero_elemento = int(input("Ingrese el número del elemento a modificar: "))
        if numero_elemento < len(mi_lista):
            elemento_nuevo = input("Ingrese el nuevo valor del elemento: ")
            mi_lista[numero_elemento] = elemento_nuevo
            print("Elemento modificado con éxito!")
        else:
            print("Número fuera de rango!")

    elif opcion == "3":
        numero_elemento = int(input("Ingrese el número del elemento a eliminar: "))
        if numero_elemento < len(mi_lista):
            mi_lista[numero_elemento]
            print("Elemento eliminado con éxito!")
        else:
            print("Número fuera de rango!")

    elif opcion == "4":
        if len(mi_lista) > 0:
            mi_lista[-1]
            print("Último elemento eliminado con éxito!")
        else:
            print("La lista está vacía!")

    elif opcion == "5":
        elemento = input("Ingrese el elemento a buscar: ")
        encontrado = False
        for x in range(len(mi_lista)):
            if mi_lista[x] == elemento:
                print("Elemento encontrado en la posición " + str(x) + "!")
                encontrado = True
                break
        if not encontrado:
            print("Elemento no encontrado!")

    elif opcion == "6":
        print("Elementos de la lista:")
        for x in range(len(mi_lista)):
            print(str(x) + ": " + mi_lista[x])

    elif opcion == "7":
        print("Adiós!")
        break

    else:
        print("Opción inválida. Intente nuevamente!")