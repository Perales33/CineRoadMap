# 🎬 CineRoadmap – El reto final para los cinéfilos

**CineRoadmap** es una plataforma web gamificada desarrollada con Flask que permite a los amantes del cine registrar las películas que han visto, desbloquear insignias y completar desafíos cinematográficos. Inspirada en los logros de videojuegos, promueve el descubrimiento fílmico y el espíritu comunitario entre cinéfilos.


## 📌 Tabla de Contenidos

- [🚀 Características principales ](#características-principales)
- [🏆 Insignias y logros](#insignias-y-logros)
- [Desafíos diarios y semanales](#desafíos-diarios-y-semanales)
- [Perfil y comunidad](#perfil-y-comunidad)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Próximos pasos](#próximos-pasos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)


## 🚀 Características principales 

- Registro y consulta de películas vistas.
- Sistema de insignias por logros cinematográficos.
- Desafíos diarios/semanales que incentivan el hábito.
- Perfil con estadísticas, rachas y horas de visualización.
- Comparación con amigos y comunidad.


## 🏆 Insignias y logros

### 🎥 Colecciones
- **Top 100 IMDb**
- **Oscar 2024**
- **Cinéfilo Retro**
- **Cine Independiente**

### 👥 Actores y Directores
- **Fan de Scorsese**
- **Fan de Christian Bale**

### 🕰️ Por Décadas
- **Cinéfilo de los 60**
- **Rey del VHS (80s)**
- **Nostalgia 90s**

### 🧗 Retos Especiales
- **Semana de cine**
- **1 Day 1 Saga**
- **365 películas al año**


## 📅 Desafíos diarios y semanales

- 🎯 **Recomendación diaria** automática.
- 🧭 **Reto del día** (Ej. ver película de un país nuevo).
- 🎥 **Reto semanal** (Ej. película nominada al Oscar).
- 🤝 **Reto comunitario** para compartir con amigos.


## 👤 Perfil y comunidad

- Lista de películas vistas.
- Insignias desbloqueadas.
- Estadísticas cinéfilas:
  - Películas totales
  - Racha más larga
  - Mes más productivo
  - Total de horas
- Comparte logros y progreso con amigos.


## 🛠️ Tecnologías utilizadas

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JavaScript (desde `templates` y `static`)
- **Base de datos**: SQLite (con backup incluido)
- **Librerías clave**:
  - `Flask`
  - `Werkzeug`


## ⚙️ Instalación y ejecución

### 🔧 Requisitos
```bash
- Python 3.8+
- pip
```

### 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Perales33/Cineroadmap.git
cd Cineroadmap
```

2. Instala los requerimientos

```bash
pip install -r requirements.txt
```

3. Ejecuta la app

```bash
flask run -p 5000
```
4. Abre tu navegador y accede a: 
```bash
http://127.0.0.1:5000/
``` 

### 📁 Estructura del proyecto
```bash
Cineroadmap/
├── app.py                  # Archivo principal Flask
├── ddbb 
│   ├── movies.db           # Base de datos SQLite
│   └── backup.db           # Backup de la base de datos
├── requirements.txt        # Dependencias (Flask, Werkzeug)
├── LICENSE                 # Licencia del proyecto
├── README.md               # Este archivo
├── Datos/                  # Archivos CSV de soporte
├── templates/              # HTML renderizado por Flask
├── static/                 # CSS, JavaScript, imágenes
│   ├── css/
│   ├── js/
│   └── img/
```

### 🔮 Próximos pasos

- Migrar la aplicación a Java
- Desarrollar la aplicación para móvil
- Integración con APIs externas (IMDb o TMDB)
- Versión móvil (Android/iOS)
- Sincronización entre dispositivos
- Sistema de notificaciones

### 📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.