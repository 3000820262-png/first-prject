# Módulo tarea.py
# Define la clase Tarea - representa una tarea individual

class Tarea:
    """
    Clase que representa una tarea individual.
    
    Atributos:
        id (int): Identificador único de la tarea
        titulo (str): Título o descripción de la tarea
        completada (bool): Si la tarea está hecha o no
    """
    
    def __init__(self, id, titulo):
        """
        Constructor de la clase Tarea.
        Se ejecuta cuando creamos una nueva Tarea.
        
        Args:
            id (int): Número único para esta tarea
            titulo (str): Lo que hay que hacer
        """
        self.id = id
        self.titulo = titulo
        self.completada = False  # Por defecto, las tareas no están hechas
    
    def marcar_como_completada(self):
        """
        Método que marca la tarea como hecha.
        """
        self.completada = True
        print(f"✅ Tarea '{self.titulo}' marcada como completada.")
    
    def marcar_como_pendiente(self):
        """
        Método que marca la tarea como pendiente (no hecha).
        """
        self.completada = False
        print(f"⏳ Tarea '{self.titulo}' marcada como pendiente.")
    
    def obtener_estado(self):
        """
        Método que retorna el estado actual de la tarea.
        
        Returns:
            str: Una descripción del estado de la tarea
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"[{estado}] {self.titulo}"
    
    def __str__(self):
        """
        Método especial que define cómo se representa la tarea en texto.
        Se usa cuando haces print(tarea).
        """
        simbolo = "✓" if self.completada else "○"
        return f"{simbolo} ID: {self.id} | {self.titulo}"
