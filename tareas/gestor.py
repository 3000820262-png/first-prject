# Módulo gestor.py
# Define la clase Gestor - controla todas las tareas

from tareas.tarea import Tarea

class Gestor:
    """
    Clase Gestor que maneja todas las tareas.
    Se encarga de agregar, eliminar, actualizar y listar tareas.
    
    Atributos:
        tareas (list): Lista que almacena todos los objetos Tarea
        proximo_id (int): Contador para asignar IDs únicos
    """
    
    def __init__(self):
        """
        Constructor del Gestor.
        Inicializa una lista vacía de tareas.
        """
        self.tareas = []      # Lista vacía para guardar tareas
        self.proximo_id = 1   # Próximo ID a asignar
    
    def agregar_tarea(self, titulo):
        """
        Método que agrega una nueva tarea a la lista.
        
        Args:
            titulo (str): Descripción de la tarea
        
        Returns:
            Tarea: La tarea que fue creada
        """
        nueva_tarea = Tarea(self.proximo_id, titulo)
        self.tareas.append(nueva_tarea)  # Añadir a la lista
        self.proximo_id += 1              # Incrementar para la próxima tarea
        print(f"✏️  Tarea agregada: '{titulo}' (ID: {nueva_tarea.id})")
        return nueva_tarea
    
    def obtener_tarea(self, id):
        """
        Método que busca una tarea por su ID.
        
        Args:
            id (int): El ID de la tarea que buscamos
        
        Returns:
            Tarea: La tarea encontrada, o None si no existe
        """
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None
    
    def eliminar_tarea(self, id):
        """
        Método que elimina una tarea por su ID.
        
        Args:
            id (int): El ID de la tarea a eliminar
        
        Returns:
            bool: True si se eliminó, False si no encontró la tarea
        """
        tarea = self.obtener_tarea(id)
        if tarea:
            self.tareas.remove(tarea)
            print(f"🗑️  Tarea eliminada: '{tarea.titulo}'")
            return True
        print(f"❌ No encontré tarea con ID {id}")
        return False
    
    def listar_todas(self):
        """
        Método que muestra todas las tareas.
        """
        if not self.tareas:
            print("\n📭 No hay tareas. ¡Crea una para empezar!\n")
            return
        
        print("\n📋 LISTA DE TAREAS:")
        print("=" * 50)
        for tarea in self.tareas:
            print(f"  {tarea}")  # Usa el método __str__ de Tarea
        print("=" * 50 + "\n")
    
    def contar_tareas(self):
        """
        Método que retorna cuántas tareas hay en total.
        
        Returns:
            int: Número total de tareas
        """
        return len(self.tareas)
    
    def contar_completadas(self):
        """
        Método que cuenta cuántas tareas están completadas.
        
        Returns:
            int: Número de tareas completadas
        """
        completadas = 0
        for tarea in self.tareas:
            if tarea.completada:
                completadas += 1
        return completadas
    
    def obtener_resumen(self):
        """
        Método que retorna un resumen del estado.
        
        Returns:
            str: Resumen con estadísticas
        """
        total = self.contar_tareas()
        completadas = self.contar_completadas()
        pendientes = total - completadas
        
        return f"Total: {total} | Completadas: {completadas} | Pendientes: {pendientes}"
