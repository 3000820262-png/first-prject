# Paquete tareas
# Este archivo hace que Python reconozca 'tareas' como un paquete
# Aquí podemos importar clases para que sean fáciles de acceder

from tareas.tarea import Tarea
from tareas.gestor import Gestor

__all__ = ['Tarea', 'Gestor']
