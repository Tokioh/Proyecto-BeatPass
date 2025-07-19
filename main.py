from usuarios import registrar_usuario
from conciertos import listar_conciertos, registrar_concierto
from boletos import generar_boleto, mostrar_boletos_usuario

def menu():
    while True:
        print("\n--- BeatPass ---")
        print("1. Registrarse")
        print("2. Ver conciertos")
        print("3. Comprar entrada")
        print("4. Ver mis boletos")
        print("5. Registrar Concierto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_conciertos()
        elif opcion == "3":
            generar_boleto()
        elif opcion == "4":
            mostrar_boletos_usuario()
        elif opcion == "5":
            registrar_concierto()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
