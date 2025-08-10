#Archivo 2 ya mas pulido que muestra mejor las opciones. Fijarse en comentarios para tener mejor guia. 
bandera=True
vuelos = []

opcion_busqueda = 0
encontrados = []
    #Lectura de datos del archivo vuelos.

with open('vuelos.txt', 'r', encoding='utf-8') as archivo: #Con el with as, a diferencia del otro modo como el propuesto por el profesor, el codigo queda mas limpio y no hay necesidad de usar el close, es una manera muy segura de usar esta funcion.
    for linea in archivo:
        datos = linea.strip().split(',')
        vuelos.append(datos) #permite anadir info

def mostrar_resultados(encontrados): #Funcion hecha para revisar y buscar por los filtros con lo que necesitamos de cada posicion. 
    if encontrados:
        print("\nVuelos encontrados:")
        for vuelo in encontrados:
            fecha = vuelo[1]
            origen = vuelo[2]
            destino = vuelo[3]
            aerolinea = vuelo[6]
            precio = vuelo[7]
            print(f"- Aerolínea: {aerolinea}, Fecha: {fecha}, Origen: {origen}, Destino: {destino}, Precio: ${precio}")
    else:
        print("\nNo se encontraron vuelos con ese criterio.") #El salto de linea \n* da mejor visualizacion del mensaje impreso.
    input("\nPresione Enter para volver al menú principal") 

# Modo búsqueda ya con el menu
bandera = True
while bandera:
    opcion_busqueda = 0
    while opcion_busqueda < 1 or opcion_busqueda > 6: #Con esto validamos que efectivamente sea alguna de las opciones y no se nos vaya a un ciclo sin fin o nos de cualquier otra cosa. 
        print("*********************************************************")
        print("Bienvenido al modo búsqueda")
        print("*********************************************************")
        print("1. Buscar por fecha de vuelo")
        print("2. Buscar por aerolínea")
        print("3. Buscar por lugar de origen")
        print("4. Buscar por lugar de destino")
        print("5. Buscar vuelos por precio máximo")
        print("6. Menú principal")
        print("*********************************************************")
        entrada = input("Ingrese la opción que desee: ").strip() #Los strip son muy utiles para ingresar datos ya que elimina espacios de linea innecesarios. Creo que seria bien agregarlo a todas las partes donde se necesite. 
        if entrada in ["1", "2", "3", "4", "5", "6"]: #El in* es sumamente util para verificar entradas en una lista. 
            opcion_busqueda = int(entrada)
        else:
            print("Opción inválida. Intente de nuevo.")

    if opcion_busqueda == 1:
        fecha = ""
        while not (len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/" and fecha.replace("/", "").isdigit()): 
            fecha = input("Ingrese la fecha de vuelo (DD/MM/AAAA): ").strip()
            if not (len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/" and fecha.replace("/", "").isdigit()): #El not* en cada una de estas lo que hace es hacer lo mismo que conocemos del while, if, y casi que cualquier palabra reservada pero al contrario. 
                print("Formato inválido. Intente nuevamente.")
        encontrados = [v for v in vuelos if v[1] == fecha]
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 2:
        aerolinea = ""
        while aerolinea == "":
            aerolinea = input("Ingrese el nombre de la aerolínea: ").strip().lower()#Cada strip lover lo que hace es que si seingresa un valor con minusculas, tambien va a ser acpetado
            if aerolinea == "":
                print("Debe ingresar un nombre válido.")
        encontrados = [v for v in vuelos if v[6].strip().lower() == aerolinea]
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 3:
        origen = ""
        while origen == "":
            origen = input("Ingrese la ciudad de origen: ").strip().lower()
            if origen == "":
                print("Debe ingresar una ciudad válida.")
        encontrados = [v for v in vuelos if v[2].strip().lower() == origen]
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 4:
        destino = ""
        while destino == "":
            destino = input("Ingrese la ciudad de destino: ").strip().lower()
            if destino == "":
                print("Debe ingresar una ciudad válida.")
        encontrados = [v for v in vuelos if v[3].strip().lower() == destino]
        mostrar_resultados(encontrados) #No estoy seguro de esta parte. Creo que hay que revisarla. 

    elif opcion_busqueda == 5:
        precio_max = ""
        while not (precio_max.isdigit() and int(precio_max) > 0):
            precio_max = input("Ingrese el precio máximo: ").strip()
            if not (precio_max.isdigit() and int(precio_max) > 0):
                print("Debe ingresar un número válido mayor que cero.")
        precio_max = int(precio_max)
        encontrados = [v for v in vuelos if int(v[7]) <= precio_max] #No estoy seguro si esta parte esta bien ya que la probe pero no funciono 
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 6:
        bandera = False  # Volver al menu principal
