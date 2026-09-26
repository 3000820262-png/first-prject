# Módulo helpers.py
# Funciones auxiliares para la aplicación

def mostrar_menu():
    """
    Función que muestra el menú principal de la aplicación.
    """
    print("\n" + "="*50)
    print("      GESTOR DE TAREAS")
    print("="*50)
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Marcar tarea como pendiente")
    print("5. Eliminar tarea")
    print("6. Ver resumen")
    print("7. Salir")
    print("="*50)

def obtener_entrada(mensaje):
    """
    Función que obtiene entrada del usuario de forma segura.
    
    Args:
        mensaje (str): El mensaje a mostrar al usuario
    
    Returns:
        str: Lo que escribió el usuario
    """
    return input(f"\n{mensaje}: ").strip()

def obtener_numero(mensaje):
    """
    Función que obtiene un número del usuario.
    Valida que sea un número entero válido.
    
    Args:
        mensaje (str): El mensaje a mostrar
    
    Returns:
        int o None: El número si es válido, None si no
    """
    try:
        return int(obtener_entrada(mensaje))
    except ValueError:
        print("❌ Por favor ingresa un número válido.")
        return None
