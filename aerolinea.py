print ("Bienvenido a su aerolina favorita")
bandera=True
while bandera:
    print("1. Modo mantenimiento")
    print("2. Modo busqueda")
    print("3. Salir")
    print("************************")
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
        print("Bienvenid@ al modo mantenimiento")
        print("1.Aerolineas")
        print("2. Vuelos")
        print("3. Menú principal")
        opcion_mantenimiento=int(input("Ingrese la opción que desee:"))

        #Arolineas
        if opcion_mantenimiento==1:
            print ("1.Incluir una nueva aerolinea")
            print ("2. Eliminar alguna aerolinea")
            print ("3. Menú Principal")

            #Incluir nueva aerolinea
            opcion_mantenimiento2= int(input("Ingrese la opcion que desee:"))
            if opcion_mantenimiento2==1:
                print ("Gracias por preferirnos, ingrese el nombre de la nueva aerolinea")
                print ("****************************************************************")
                
                nuevo_nombre=input("Ingrese el nombre aquí:").lower()
                existe=False
                
                for aerolinea in aerolineas:
                    if nuevo_nombre==aerolinea[1].strip().lower():
                        existe= True
    
                if existe==True:
                    print("La aerolinea ingresada, ya se habia registrado")
                    bandera= True
                    
                else:
                    
                    with open('aerolineas.txt', 'a', encoding='utf-8') as archivo:
                        archivo.write (f"{nuevo_id},{nuevo_nombre.title()}\n")
                        print (f"Aerolinea agregada: {nuevo_id},{nuevo_nombre.title()}")

                    bandera= True
                    
            #Eliminar aerolinea
            if opcion_mantenimiento2==2:
                nombre_eliminar=input("Perfecto, ¿cual aerolinea desea eliminar?").strip().lower()
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
                    print (f"La aerolinea, {nombre_eliminar} se elimino correctamente")

                else:
                    print ("Esa aerolinea no se encuentra registrada")
                    bandera= True
            #Volver al menu 
            if opcion_mantenimiento2==3:
                    bandera= True
                
        #Vuelos
        if opcion_mantenimiento==2:
            bandera= True
            
        #Volver al menu 
        if opcion_mantenimiento2==3:
                bandera= True
                





    #Modo busqueda
    if opcion==2:
        bandera= True



    if opcion==3:
        print ("Muchas gracias por confiar en nosotros, lo esperamos pronto")
        bandera= False
        

    
