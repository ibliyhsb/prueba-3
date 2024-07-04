import csv
habitaciones=[]

with open('habitaciones.csv', 'r', newline='')as archivo_csv:
    reader=csv.reader(archivo_csv)
    for fila in reader:
        habitaciones.append(fila)

print(habitaciones)
#def reservar_habitacion(nombre, apellido, rut, fecha_hora_ingreso, fecha_hora_salida, num_habitacion):
#
#
#    
#while True:
#    try:
#        opcion=int(input("ingrese una opcion: \n1)Reservar habitación \n2) Buscar Habitación \n3) Ver estado \n4) Ventas diarias \n5)Guardar \n6)Salir \n"))
#        if opcion==1:
#            nombre=input("ingrese su nombre: ")
#            apellido=input("ingrese su apellido: ")
#            rut=input("ingrese su rut: ")
#            fecha_hora_ingreso=input("ingrese hora y fecha de ingreso: ")
#            fecha_hora_salida=input("ingrese fecha y hora de salida: ")
#            num_habitacion=int(input("ingrese el numero de la habitacion que desea reservar: "))
#            reservar_habitacion(nombre, apellido, rut, fecha_hora_ingreso, fecha_hora_salida, num_habitacion)
#    except ValueError:
#        print("ingrese valor valido")
#    else:
#        break
