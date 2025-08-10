#Esqueleto modo busqueda no se si realmente funciona porque no he podido probarlo. Por eso es solo un esqueleto. 
print("*********************************************************")
print("Bienvenido al modo búsqueda")
print("*********************************************************")
print("1. Buscar por fecha de vuelo")
print("2. Buscar por aerolínea")
print("3. Buscar por lugar de origen")
print("4. Buscar por lugar de destino")
print("5. Buscar vuelos por precio maximo")
print("6. Menú principal")
print("*********************************************************") #Creo que se ve mejor con esta presentacion de los asteriscos. 
opcion_busqueda = int(input("Ingrese la opción que desee: "))
bandera=True
vuelos = []
encontrados = []
    #Lectura de datos del archivo vuelos.

with open('vuelos.txt', 'r', encoding='utf-8') as archivo: #Con el with as, a diferencia del otro modo como el propuesto por el profesor, el codigo queda mas limpio y no hay necesidad de usar el close, es una manera muy segura de usar esta funcion.
    for linea in archivo:
        datos = linea.strip().split(',')
        vuelos.append(datos)

     #Aplicacion del filtro para cada area.

while bandera:
    
    if opcion_busqueda == 1:
        fecha = input("Ingrese la fecha de vuelo (DD/MM/AAAA): ").strip() #esto lo que hace es hacerlo en una linea eliminando espacios en blanco por si los hubieran
        encontrados = [v for v in vuelos if v[1] == fecha] #recorre y busca por indice con el for asi para cada filtro. 

    elif opcion_busqueda == 2:
        aerolinea = input("Ingrese el nombre de la aerolínea: ").strip().lower()
        encontrados = [v for v in vuelos if v[6].strip().lower() == aerolinea]#hice todo junto aplicando el for y el if para no hacer un chorizo tan largo. El lower es para que si se ingresa en letras mayus o minus lo detecte 

    elif opcion_busqueda == 3:
        origen = input("Ingrese la ciudad de origen: ").strip().lower()
        encontrados = [v for v in vuelos if v[2].strip().lower() == origen]

    elif opcion_busqueda == 4:
        destino = input("Ingrese la ciudad de destino: ").strip().lower()
        encontrados = [v for v in vuelos if v[3].strip().lower() == destino]

    elif opcion_busqueda == 5:
        precio_max = int(input("Ingrese el precio máximo: "))
        encontrados = [v for v in vuelos if int(v[7]) <= precio_max] #Creo que hay que revisar la posicion de los conjuntos. Me parece que esta bien. 
        
    elif opcion_busqueda == 6: #Siempre me da problemas de indentacion entonces no se donde poner este elif para que de verdad se devuelva al inicio
        bandera=False
    else:
        print("Opción no válida.")

    #Resultados de las consultas. 

    if encontrados:
        print("Vuelos encontrados:")
        for vuelo in encontrados:
            print(f"Aerolínea: {vuelo[6]}, Fecha: {vuelo[1]}, Origen: {vuelo[2]}, Destino: {vuelo[3]}, Precio: ${vuelo[7]}")#No estoy seguro si esto esta bien, podriamos revisarlo. No solo esta liena sino todo lo que esta en esta parte de resultados. 
    else:
        print("No se encontraron vuelos con ese criterio.")
       
