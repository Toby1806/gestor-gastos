def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")

def main():
    tareas = []
    
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-3): ")
        
        if opcion == "1":
            print("\n📋 Tus tareas actuales:")
            if not tareas:
                print("No hay tareas pendientes.")
            else:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
                    
        elif opcion == "2":
            nueva_tarea = input("\nEscribe la nueva tarea: ")
            if nueva_tarea.strip():
                tareas.append(nueva_tarea)
                print(f"✅ Tarea agregada con éxito.")
            else:
                print("⚠️ La tarea no puede estar vacía.")
                
        elif opcion == "3":
            print("\n¡Hasta luego! Saliendo del gestor...")
            break
        else:
            print("❌ Opción no válida. Por favor elige entre 1 y 3.")

if __name__ == "__main__":
    main()