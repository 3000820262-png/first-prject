#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py - Punto de entrada de la aplicación de Gestión de Tareas

Este es el archivo principal que ejecuta la aplicación.
Demostración de:
- Importación de módulos locales (tareas, utils)
- Uso de clases (Tarea, Gestor)
- Uso de funciones
- Programación Orientada a Objetos (POO)
"""

# Importar las clases desde el paquete 'tareas'
from tareas import Gestor

# Importar funciones desde el paquete 'utils'
from utils import mostrar_menu, obtener_entrada
from utils.helpers import obtener_numero


def main():
    """
    Función principal que ejecuta la aplicación.
    Controla el flujo del programa.
    """
    print("\n🎯 Bienvenido al Gestor de Tareas\n")
    
    # Crear un objeto de tipo Gestor
    # Este objeto contendrá todas nuestras tareas
    gestor = Gestor()
    
    # Agregar algunas tareas de ejemplo
    gestor.agregar_tarea("Aprender POO en Python")
    gestor.agregar_tarea("Entender clases y objetos")
    gestor.agregar_tarea("Practicar con importaciones")
    
    # Bucle principal de la aplicación
    while True:
        mostrar_menu()
        opcion = obtener_entrada("Elige una opción (1-7)")
        
        # OPCIÓN 1: Agregar tarea
        if opcion == "1":
            titulo = obtener_entrada("¿Qué tarea quieres agregar?")
            if titulo:
                gestor.agregar_tarea(titulo)
            else:
                print("❌ La tarea no puede estar vacía.")
        
        # OPCIÓN 2: Ver todas las tareas
        elif opcion == "2":
            gestor.listar_todas()
        
        # OPCIÓN 3: Marcar como completada
        elif opcion == "3":
            gestor.listar_todas()
            id_tarea = obtener_numero("Ingresa el ID de la tarea a marcar como completada")
            if id_tarea is not None:
                tarea = gestor.obtener_tarea(id_tarea)
                if tarea:
                    tarea.marcar_como_completada()
                else:
                    print(f"❌ No encontré tarea con ID {id_tarea}")
        
        # OPCIÓN 4: Marcar como pendiente
        elif opcion == "4":
            gestor.listar_todas()
            id_tarea = obtener_numero("Ingresa el ID de la tarea a marcar como pendiente")
            if id_tarea is not None:
                tarea = gestor.obtener_tarea(id_tarea)
                if tarea:
                    tarea.marcar_como_pendiente()
                else:
                    print(f"❌ No encontré tarea con ID {id_tarea}")
        
        # OPCIÓN 5: Eliminar tarea
        elif opcion == "5":
            gestor.listar_todas()
            id_tarea = obtener_numero("Ingresa el ID de la tarea a eliminar")
            if id_tarea is not None:
                gestor.eliminar_tarea(id_tarea)
        
        # OPCIÓN 6: Ver resumen
        elif opcion == "6":
            resumen = gestor.obtener_resumen()
            print(f"\n📊 RESUMEN: {resumen}\n")
        
        # OPCIÓN 7: Salir
        elif opcion == "7":
            print("\n👋 ¡Hasta luego!\n")
            break
        
        # Opción inválida
        else:
            print("❌ Opción no válida. Por favor, elige un número entre 1 y 7.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
