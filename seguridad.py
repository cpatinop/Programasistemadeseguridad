
usuarios_conocidos = ["Camilo", "Andrea","Angie","Nicolas", "Adrew", "Bob"]
print(str(len(usuarios_conocidos))+ "  Estos son la cantidad de user en la lista") # Cuantos elementos hay en la lista

while True:
    print("Hola mi nombre es bot")
    nombre = input ( "Cual es tu nombre?:  ".strip().capitalize()) # De esta forma pedimos datos por consola, y lo guardamos en la variable nombre
    if nombre in usuarios_conocidos:  # Validacion del input ingresado en la lista previamente creada 
        print("Hola {}!".format(nombre)) # Cadena de texto
        eliminar = input("Quieres ser Eliminado(y/n)?:  ").strip().lower() 
        if eliminar == "y":
            usuarios_conocidos.remove(nombre)
        elif eliminar == "n":
            print( "No hay problema")
    else:
        print("Umm.. no creo haberte conocido aun {}".format(nombre))
        agregar = input ("Te gustaria ser agregado a la lista (y/n)?:  ").strip().lower()
        if agregar == "y":
            usuarios_conocidos.append(nombre)
        elif agregar == "n":
            print( "Dios te bendiga...")    