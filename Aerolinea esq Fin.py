print("\n""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("|              BIENVENIDO A LOOK&FLY                |")
print("|            Tu buscador de vuelos confiable             |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

bandera=True
while bandera:
    print("1. Modo mantenimiento")
    print("2. Modo busqueda")
    print("3. Salir")
    print("*********************************************************")
    opcion=int(input("Ingrese la opción que desee:"))

    #Leer el archivo y guardar

    aerolineas=[]
    #encondinf='utf-8' se usa para leer caracteres, o escribir.
    #Si no ponés encoding='utf-8', Python usa la codificación predeterminada
    #del sistema operativo.
    with open ('aerolineas.txt','r',encoding='utf-8') as archivo:
        for linea in archivo:
            datos= linea.strip().split(',')#lo separa por comas, y quita los parrafos
            aerolineas.append(datos)
        for a in aerolineas:
            print (a)
            
        if aerolineas:
            ultimo_id=int(aerolineas[-1][0])
            
        else:
            ultimo_id=0
        nuevo_id= ultimo_id+1



   
    #Modo Mantenimiento           
    if opcion==1:
        print("*********************************************************")
        print("Bienvenid@ al modo mantenimiento")
        print("1.Aerolineas")
        print("2. Vuelos")
        print("3. Menú principal")
        opcion_mantenimiento=int(input("Ingrese la opción que desee:"))

        #Arolineas
        if opcion_mantenimiento==1:
            print("*********************************************************")
            print ("1.Incluir una nueva aerolinea")
            print ("2. Eliminar alguna aerolinea")
            print ("3. Menú Principal")

            #Incluir nueva aerolinea
            opcion_mantenimiento2= int(input("Ingrese la opcion que desee:"))
            if opcion_mantenimiento2==1:
                print("*********************************************************")
                print ("Gracias por preferirnos, ingrese el nombre de la nueva aerolinea")
                print("*********************************************************")
                
                nuevo_nombre=input("Ingrese el nombre aquí:").lower()
                existe=False
                
                for aerolinea in aerolineas:
                    if nuevo_nombre==aerolinea[1].strip().lower():
                        existe= True
    
                if existe==True:
                    print("*********************************************************")
                    print("La aerolinea ingresada, ya se habia registrado")
                    bandera= True
                    
                else:
                    
                    with open('aerolineas.txt', 'a', encoding='utf-8') as archivo:
                        archivo.write (f"{nuevo_id},{nuevo_nombre.title()}\n")
                        print("*********************************************************")
                        print (f"Aerolinea agregada: {nuevo_id},{nuevo_nombre.title()}")

                    bandera= True
                    
            #Eliminar aerolinea
            if opcion_mantenimiento2==2:
                print("*********************************************************")
                nombre_eliminar=input("Perfecto, ¿Cual aerolinea desea eliminar?").strip().lower()
                lista=[] #nueva lista donde se van a sobre escribir las aerolineas
                orden=1
                
                existe=False
                
                for aerolinea in aerolineas: #Revisar si la aerolinea si esta registrada, o no
                    if nombre_eliminar==aerolinea[1].strip().lower():
                        existe= True
    
                if existe==True:
                                   
                    for aerolinea in aerolineas:
                        if aerolinea[1].strip().lower() != nombre_eliminar: #aqui se sobre escriben 1 por 1 las aerolineas que sean diferentes a la aerolinea que se desea borrar
                            lista.append([str(orden), aerolinea[1].strip()])
                            orden +=1
                        

                    with open ('aerolineas.txt', 'w', encoding='utf-8') as archivo: #con esto se sobre escribe el archivo aerolineas.txt
                        for aerolinea in lista:
                            archivo.write(','.join(aerolinea)+'\n')
                    print("*********************************************************")
                    print (f"La aerolinea, {nombre_eliminar} se ha eliminado correctamente")

                else:
                    print("*********************************************************")
                    print ("Esa aerolinea no se encuentra registrada")
                    bandera= True
            #Volver al menu 
            if opcion_mantenimiento2==3:
                    bandera= True
                
        #Vuelos
        if opcion_mantenimiento==2:
            print("*********************************************************")
            print ("Bienvend@ al modulo de mantenimiento")
            print ("1.Incluir una nueva aerolinea")
            print ("2.Eliminar alguna aerolinea")
            print ("3.Menú principal")
            print("*********************************************************")
            opcion_vuelos=int(input("Ingrese la opción que desee:"))
    
            if opcion_vuelos==1:
                existe=False #revisar si ya esa aerolinea esta inscrita, para poder ingresar un vuelo
                print("*********************************************************")
                print ("Gracias por preferirnos")
                nombre_vuelo= input("Ingrese el nombre de la aerolinea:").strip().lower()
                for aerolinea in aerolineas:
                    if aerolinea[1].strip().lower()==nombre_vuelo:
                        existe=True
                        
                if existe:
                    print("*********************************************************")
                    
                    
                    numero_vuelo=input("Ingrese el numero de vuelo aqui:")
                    fecha_vuelo=input("Ingrese la fecha aquí(dia/mes/año):")
                    origen_vuelo=input("Ingrese el origen aquí(En codigo internacional):")
                    destino_vuelo=input("Ingrese el destino aquí(En codiifo internacional):")
                    hora_salida= input("Ingrese la hora en que sale el vuelo(En formato militar):")
                    hora_llegada=input("Ingrese la hora de llegada(En formato militar):")
                    costo_vuelo= int(input("Ingrese el costo del viaje($):"))
                    print("*********************************************************")

                    ID=None #Se crea una variable basia
                    for aerolinea in aerolineas: #Se reutiliza el "arolineas=[] que se hizo al puro inicio"
                        if aerolinea[1].strip().lower()==nombre_vuelo: #Revisar si la posicion de la aeroliena en el archivo aerolineas.txt, es igual al vuelo que se quiere registrar
                            ID= aerolinea[0] 

                                
                            
                
        
                    with open ('vuelos.txt','a',encoding='utf-8')as archivo:
                        #aqui escribe el archivo, segun el orden del formato de los vuelos, con los datos que le pedimos anteriormente
                        #el "\n" al inicio para brincar de renglon
                        archivo.write("\n"+f"{numero_vuelo},{fecha_vuelo},{origen_vuelo},{destino_vuelo},{hora_salida},{hora_llegada},{ID},{costo_vuelo}") 
                        print("*********************************************************")
                        print ("Vuelo agregado correctamente")
                        print("*********************************************************")
                        
                    bandera= True
                    
                    
                else:
                    print("*********************************************************")
                    print("Esta aerolinea no se encuentre inscrita, primero debes registrarla")
                    bandera=True
                


            if opcion_vuelos==2:
                vuelos=[] #en esta lista se van a guardas todos los vuelos disponibles
                with open ('vuelos.txt','r', encoding='utf-8')as archivo2:
                    for linea in archivo2:
                        datos2=linea.strip().split(',')#crea una variable con todos los vuelos, separandolos por ','
                        vuelos.append(datos2)#aqui se guardan
                    for b in vuelos:
                        print(b)
                vuelo_eliminar=input("¿Cual de los anteriores vuelos desea eliminar, segun su codigo de aerolinea?").strip().lower()

                
                lista2=[] #aqui se va a guardar la nueva lista de vuelos, eliminando el vuelo ingresado
                for vuelo in vuelos:
                    if vuelo[0].strip().lower() != vuelo_eliminar: #busca el codigo de vuelo que sea igual, al ingresado por el usuario,para saltarselo
                        lista2.append(vuelo)
                                     
                with open('vuelos.txt','w',encoding='utf-8')as archivo2:
                    for vuelo in lista2:
                        archivo2.write (','.join(vuelo)+'\n')
                print("*********************************************************")
                print (f"El vuelo con codigo:{vuelo_eliminar} se elimino correctamente")
                
                        
                    

            if opcion_vuelos==3:
                bandera=True

                
        #Volver al menu 
        if opcion_mantenimiento==3:
            bandera= True
                



    #Modo busqueda (Hay que hacer una funcion para conectar me parece o algo para que logre conectar esta parte del codigo)
    if opcion==2:
        bandera=True
        vuelos = []
        opcion_busqueda = 0
        encontrados = []
    #Lectura de datos del archivo vuelos.

with open('vuelos.txt', 'r', encoding='utf-8') as archivo: #Con el with as, a diferencia del otro modo como el propuesto por el profesor, el codigo queda mas limpio y no hay necesidad de usar el close, es una manera muy segura de usar esta funcion.
    for linea in archivo:
        datos = linea.strip().split(',')
        vuelos.append(datos) #hace que el archivo se convierta en lista de listas para asi poder trabajar de manera adecuada. 

def mostrar_resultados(encontrados): #Funcion hecha para revisar y exponer por los filtros. Ordena los resultados y los imprime mas adecuadamente.  
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

def pedir_entero_positivo(mensaje):#funcion hecha para validar entrada en precios que sea en numeros y que sea mayor que 0
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("Debe ingresar un número válido mayor que cero.")

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
        fecha = "" #cadena vacia para llenar con resultados
        while not (len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/" and fecha.replace("/", "").isdigit()): #Mientras la fecha no cumpla con ese formato, seguir pidiendo al usuario que la ingrese (mantiene el ciclo)
            #el .replace y el .isdigit son muy utiles para validar. En el sentido que el .replace lo que hace es reemplazar digitos de una cadena y el .isdigit validar que efectivamente sean numeros. Esto elimina muchas funciones necesarias para validacion 
        #cadena.replace("A", "B") y cadena.isdigit() (devuelve T o F)
 
            fecha = input("Ingrese la fecha de vuelo (DD/MM/AAAA): ").strip()
            if not (len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/" and fecha.replace("/", "").isdigit()): #El not* en cada una de estas lo que hace es hacer lo mismo que conocemos del while, if, y casi que cualquier palabra reservada pero al contrario. 
                print("Formato inválido. Intente nuevamente.") #Validacion de que la fecha este bien realmente y si no arroja error. 
        encontrados = [v for v in vuelos if v[1] == fecha]
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 2: #Busqueda aerolinea pero por ID no por nombre
        aerolinea = ""#lista vacia
        while aerolinea == "":
            aerolinea = input("Ingrese el nombre de la aerolínea: ").strip().lower()#Cada strip lover lo que hace es que si seingresa un valor con minusculas, tambien va a ser acpetado
            if aerolinea == "":
                print("Debe ingresar un nombre válido.")
        encontrados = [v for v in vuelos if v[6].strip().lower() == aerolinea]
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 3: #Busqueda por ciudad de origen
        origen = ""
        while origen == "":
            origen = input("Ingrese la ciudad de origen: ").strip().lower()
            if origen == "":
                print("Debe ingresar una ciudad válida.")
        encontrados = [v for v in vuelos if v[2].strip().lower() == origen]
        mostrar_resultados(encontrados)

    elif opcion_busqueda == 4: #Busqueda por ciudad de destino
        destino = ""
        while destino == "":
            destino = input("Ingrese la ciudad de destino: ").strip().lower()
            if destino == "":
                print("Debe ingresar una ciudad válida.")
        encontrados = [v for v in vuelos if v[3].strip().lower() == destino]
        mostrar_resultados(encontrados) 

    elif opcion_busqueda == 5:  # Busqueda por precio
        precio_max = pedir_entero_positivo("Ingrese el precio máximo: ")
        encontrados = [v for v in vuelos if v[7].isdigit() and int(v[7]) <= precio_max]
        mostrar_resultados(encontrados)


    elif opcion_busqueda == 6:
        bandera = False  # Volver al menu principal


#Hay que mejorar esta parte porque igual imprime todo y no deberia. 
    if opcion==3:
        print ("Muchas gracias por confiar en Look&Fly, lo esperamos pronto")
        bandera= False
        

    
