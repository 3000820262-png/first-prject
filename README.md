# Aplicación de Gestión de Tareas

Una aplicación básica en Python para aprender:
- **POO** (Programación Orientada a Objetos)
- **Funciones**
- **Importación de librerías locales**
- **Estructura de proyecto**

## Estructura del Proyecto

```
first-prject/
├── main.py              # Punto de entrada de la aplicación
├── tareas/              # Paquete con la lógica de tareas
│   ├── __init__.py      # Hace que sea un paquete Python
│   ├── tarea.py         # Clase Tarea (modelo de datos)
│   └── gestor.py        # Clase Gestor (lógica principal)
└── utils/               # Paquete con funciones auxiliares
    ├── __init__.py
    └── helpers.py       # Funciones de ayuda
```

## Cómo ejecutar

```bash
python main.py
```

## Conceptos que aprenderás

1. **Clases y Objetos** → `Tarea` y `Gestor`
2. **Métodos** → Funciones dentro de clases
3. **Atributos** → Datos almacenados en objetos
4. **Importaciones locales** → Importar módulos de tu propio proyecto
5. **Funciones** → Código reutilizable
