import os
os.system('cls' if os.name == 'nt' else 'clear')

libros= []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pasuar():
    input("precione Enter para continuar...")

def menu():
    print("                🔱===== MENU =====🔱                   ")
    print("✨--- Sistema de Gestión de Biblioteca Persona ---✨")
    print("1.Agregar Libro")
    print("2.Ver Biblioteca")
    print("3.Buscador de Libros")
    print("4.Cambiar estado de Libros")
    print("5.Estadisticas")
    print("6.Eliminar libro")
    print("7.Salir")

def agregarLibro():
    print("====== Agregar nuevo Libro 📔 ======")
    ti=input("Digite el Titulo del libro: ")
    au=input("Digite el nombre del autor del libro: ")
    gen=input("Digite el genero del libro: ")
    año=int(input("Digite el año de publicacion del libro: "))
    estado=input("el libro a sido leido? (s/n): ").lower()
    
    if estado == "s":
        estado=True
    
    elif estado == "n":
        estado=False

    else :
        print("⚠️ seleccione una opcion valida ⚠️")

    New=[ti,au,gen,año,estado]
    libros.append(New)

    print("El libro fue agregado con exito ✅")

def leerBiblioteca():
    print("====== Biblioteca 📚 ======".center(50))

    if libros:

        for i, libro in enumerate(libros):
            titulo = libro[0]
            nombre = libro[1]      
            genero = libro[2]      
            año = libro[3]  
            leido = libro [4]    
            estado = "✓" if leido else "✗"
            print(f"{i+1}. titulo: {titulo} | nombre: {nombre} | genero: {genero} | año: {año} | Estado: {estado} | ")
            

    else :
        print("no hay libros en la biblioteca")

def buscar_libros(palabra):
    sugerencias = []
    for libro in libros:
        titulo, autor, genero, _, _ = libro
        if palabra.lower() in titulo.lower() or palabra.lower() in autor.lower() or palabra.lower() in genero.lower():
            sugerencias.append(libro)
    return sugerencias

def estadoLibro():
    leerBiblioteca()

    num=int(input("ingrese el numero del libro que desea marcar como leido: "))
    num= num - 1

    if 0<= num < len(libros):

        libros[num][4]= not libros[num][4]
        estado ="✓" if libros[num][4] else "✗"
        print(f"✅ el cambio fue completado con exitosamente")
    

    
    else :
        print("error intente de nuevo")










isActive=True
while isActive:
    menu()
    try: 
        opcion=int(input("digite una opcion del 1-7: "))
        clear_screen()
        match opcion:

            case 1:
                agregarLibro()
                pasuar()
                clear_screen()

            case 2:
                
                leerBiblioteca()
                pasuar()
                clear_screen()

            case 3:
                
                entrada = input("\n🔎 Buscar libros por título, autor o género: ")
                resultados = buscar_libros(entrada)
                if resultados:
                    print("\n📚 Resultados encontrados:")
                    for i, libro in enumerate(resultados, 1):
                        print(f"{i}. titulo: {libro[0]} | Autor: {libro[1]} | Genero: {libro[2]}")
                else:
                    print("❌ No se encontraron coincidencias.")
                pasuar()
                clear_screen()

            case 4:
                
                estadoLibro()
                pasuar()
                clear_screen()

            case 5:
                pass

            case 6:
                pass

            case 7:
                print("Gracias por usar Sistema de Gestión de Biblioteca")
                pasuar()
                isActive=False

            case _:
                pass


















    except ValueError: 
        print("erro")