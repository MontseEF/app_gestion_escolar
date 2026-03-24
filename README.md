# 📚 Sistema de Gestión Escolar

Aplicación web desarrollada con Django para la administración de alumnos, cursos y profesores, utilizando base de datos MySQL y preparada para despliegue en entorno productivo.

---

## 🚀 Tecnologías utilizadas

* 🐍 Python 3.13
* 🌐 Django 6
* 🗄️ MySQL
* 🔐 Django Authentication
* ⚙️ python-decouple (manejo de variables de entorno)
* 🧪 Virtual Environment (.venv)

---

## 📌 Funcionalidades principales

* ✔️ Gestión de alumnos
* ✔️ Gestión de profesores
* ✔️ Gestión de cursos
* ✔️ Panel administrativo de Django
* ✔️ Autenticación de usuarios (login/logout)
* ✔️ Migraciones de base de datos
* ✔️ Configuración para entorno de producción

---

## 🧩 Estructura del proyecto

```
app_gestion_escolar/
│
├── GestionEscolar/        # Configuración principal del proyecto
├── alumnos/               # App de alumnos
├── profesores/            # App de profesores
├── cursos/                # App de cursos
├── templates/             # Plantillas HTML
├── .venv/                 # Entorno virtual (no subir)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```
git clone https://github.com/TU_USUARIO/app_gestion_escolar.git
cd app_gestion_escolar
```

---

### 2. Crear y activar entorno virtual

```
python -m venv .venv
source .venv/Scripts/activate
```

---

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

---

### 4. Configurar variables de entorno

Crear archivo `.env` en la raíz del proyecto:

```
DB_NAME=gestion_escolar
DB_USER=root
DB_PASSWORD=TU_PASSWORD
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

### 5. Aplicar migraciones

```
python manage.py migrate
```

---

### 6. Crear superusuario

```
python manage.py createsuperuser
```

---

### 7. Ejecutar servidor

```
python manage.py runserver
```

Acceder a:
👉 http://127.0.0.1:8000/admin/

---

## 🗄️ Base de datos

El proyecto utiliza **MySQL** como motor de base de datos.

Configuración en `settings.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_escolar',
        'USER': 'root',
        'PASSWORD': 'TU_PASSWORD',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

---

## 🌐 Despliegue

El proyecto está preparado para despliegue en plataformas como:

* AlwaysData
* Render
* Railway

Incluye configuración para producción y manejo de variables de entorno.

---

## 📌 Base del proyecto

Este proyecto fue desarrollado a partir de una base inicial de:

👉 https://github.com/ffelipecuevasc/GestionEscolar

Posteriormente fue adaptado, configurado y extendido por mí, incluyendo:

* 🔧 Migración de SQLite a MySQL
* ⚙️ Configuración de entorno virtual
* 🔐 Implementación de variables de entorno
* 🚀 Preparación para despliegue
* 🧩 Ajustes en estructura del proyecto

---

## 👩‍💻 Autora

Montserrat Espinoza Flores

---

## ⭐ Notas

Este proyecto forma parte de mi portafolio como desarrolladora Full Stack en formación, enfocado en:

* Backend con Django
* Bases de datos relacionales
* Configuración de entornos reales
* Despliegue de aplicaciones web

---
