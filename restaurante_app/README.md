# Sistema de Gestión de Restaurante - POO Semana 4

## 👤 Información del Estudiante
- **Nombre Completo:** Pablo Javier Yanza Delgado
- **Asignatura:** Programación Orientada a Objetos

---

## 📝 Descripción del Sistema
Este es un programa en Python enfocado en demostrar el uso de la arquitectura modular y los pilares de la Programación Orientada a Objetos (POO). El software gestiona entidades básicas de un restaurante (`Producto` y `Cliente`) inyectándolas dentro de un servicio centralizado (`Restaurante`) encargado de controlar y mostrar la información recolectada de manera ordenada a través de la consola.

---

## 📂 Estructura y Explicación del Proyecto

El repositorio está organizado respetando la separación de responsabilidades en módulos independientes:

```text
restaurante_app/
│
├── modelos/                  # CAPA DE DATOS (Entidades puras)
│   ├── producto.py           # Define la clase Producto (atributos: nombre, precio)
│   └── cliente.py            # Define la clase Cliente (atributos: nombre, cédula)
│
├── servicios/                # CAPA DE LÓGICA DE NEGOCIO (Controladores)
│   └── restaurante.py        # Clase Restaurante: Administra el almacenamiento en memoria
│
├── main.py                   # PUNTO DE ARRANQUE (Orquestador principal)
│                             # Importa los módulos, genera los objetos de prueba
│                             # y ejecuta la demostración en consola.
└── README.md                 # Documentación técnica del repositorio