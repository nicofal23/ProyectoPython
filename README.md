# Clona el repositorio
```bash
git clone https://github.com/nicofal23/ProyectoPython.git
```
# Navega hasta la carpeta del proyecto

```bash
cd ProyectoPython
```

# Crea un entorno virtual y actívalo
```bash
pipenv shell
```

# Instala las dependencias
```bash
pip install -r requirements.txt
```

# Realiza las migraciones de la base de datos

```bash
python manage.py migrate
```

# Crea un superusuario (opcional, pero recomendado para acceder al panel de administración)

```bash
python manage.py createsuperuser
```

# Inicia el servidor de desarrollo

```bash
python manage.py runserver
```


## Funcionalidades

### 1. Gestión de Cursos

- **Crear Curso (Formulario Común):**
  - URL: `/cursos/create-comun/`
  - Permite crear un curso mediante un formulario simple.

- **Crear Curso (API):**
  - URL: `/cursos/create-api/`
  - Utiliza un formulario basado en Django Forms para crear un curso.

- **Buscar Cursos (API):**
  - URL: `/cursos/read/`
  - Permite buscar cursos por nombre utilizando un formulario de búsqueda.

### 2. Gestión de Estudiantes

- **Crear Estudiante (Formulario Común):**
  - URL: `/estudiantes/create-comun/`
  - Permite crear un estudiante mediante un formulario simple.

- **Crear Estudiante (API):**
  - URL: `/estudiantes/create-api/`
  - Utiliza un formulario basado en Django Forms para crear un estudiante.

### 3. Gestión de Profesores

- **Crear Profesor (Formulario Común):**
  - URL: `/profesores/create-comun/`
  - Permite crear un profesor mediante un formulario simple.

- **Crear Profesor (API):**
  - URL: `/profesores/create-api/`
  - Utiliza un formulario basado en Django Forms para crear un profesor.

### 4. Gestión de Entregables

- **Crear Entregable (Formulario Común):**
  - URL: `/entregables/create-comun/`
  - Permite crear un entregable mediante un formulario simple con campos para nombre, fecha de entrega y estado de entrega.

- **Crear Entregable (API):**
  - URL: `/entregables/create-api/`
  - Utiliza un formulario basado en Django Forms para crear un entregable.

## Estructura del Proyecto

- **AppCoder/views.py:** Contiene las vistas para manejar la lógica de negocio y la interacción con las plantillas.
- **AppCoder/forms.py:** Define los formularios utilizados en el proyecto.
- **AppCoder/templates/:** Contiene las plantillas HTML para las diferentes vistas.
- **urls.py:** Configuración de las rutas URL para el proyecto.


*Nicolás Falciglio*
