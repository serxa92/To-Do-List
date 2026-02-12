# ToDo API - FastAPI

API REST desarrollada con **FastAPI** para la gestión de tareas (To-Do List).  
Las tareas se almacenan en un archivo local en formato JSON, sin utilizar base de datos.

Este proyecto implementa operaciones CRUD completas y sigue una estructura modular separando modelos, lógica de almacenamiento y endpoints.

---

##  Funcionalidades

La API permite:

- ✅ Crear una tarea → `POST /tasks`
- 📋 Obtener todas las tareas → `GET /tasks`
- 🔎 Obtener una tarea por ID → `GET /tasks/{id}`
- ✔ Marcar una tarea como completada → `PUT /tasks/{id}`
- 🗑 Eliminar una tarea → `DELETE /tasks/{id}`

---

##  Modelo de datos

### Crear tarea (TaskCreate)

```json
{
  "title": "Comprar pan",
  "description": "Ir a la panadería",
  "priority": 2
}
```

- title: obligatorio
- description: opcional
- priority: Un número entre 1 y 3 (por defecto 2)
  
###  Respuesta (Task)

```json
{
  "id": 1,
  "title": "Comprar pan",
  "description": "Ir a la panadería",
  "status": "pendiente",
  "priority": 2,
  "created_at": "2026-02-12T14:45:49.695Z"
}
```


- id: generado automáticamente por el servidor
- status: "pendiente" o "completada"
- created_at: fecha de creación en formato ISO 8601 (UTC)


## ⚙ Requisitos

- Python 3.12+
- pip
- Docker Desktop (Opcional) 

##  Instalación y ejecución local
### 1️⃣ Crear entorno virtual
````python -m venv .venv````


Windows PowerShell:

````.\.venv\Scripts\Activate.ps1````

### 2️⃣ Instalar dependencias
````pip install -r requirements.txt````

### 3️⃣ Ejecutar la API
````uvicorn main:app --reload````


Acceder en navegador:

````http://127.0.0.1:8000/docs````

##  Ejecución con Docker

1️⃣ Construir imagen
````docker build -t todo-api````

2️⃣ Ejecutar contenedor
````docker run -p 8000:8000 todo-api````


Acceder en navegador:

````http://localhost:8000/docs````

## 🧪 Pruebas con Swagger o Insomnia

- Swagger está disponible automáticamente en:

  ````/docs````


- Desde Insomnia se pueden crear las siguientes requests:

  - GET http://localhost:8000/tasks
  
  - POST http://localhost:8000/tasks

  - GET http://localhost:8000/tasks/1

  - PUT http://localhost:8000/tasks/1

  - DELETE http://localhost:8000/tasks/1

##  Tecnologías utilizadas

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Docker

##  Características adicionales implementadas

- ✔ Validación de datos con Pydantic
- ✔ Restricción de prioridad (1–3)
- ✔ Fecha de creación automática
- ✔ Separación en módulos
- ✔ Soporte Docker

##  Licencia

Este proyecto está bajo la licencia MIT.


##  Autor

Desarrollado como proyecto práctico de aprendizaje de FastAPI por **[Sergio Agulla](https://www.linkedin.com/in/sergio-agulla/)**.
