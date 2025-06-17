# 🎬 Dashboard de Análisis de Contenido en Streaming
Este proyecto es una aplicación desarrollada con [Streamlit](https://streamlit.io/) para analizar, visualizar y explorar información de plataformas de streaming. Incluye estadísticas, clasificaciones por país, tipos de contenido y una navegación interactiva a través de filtros personalizables.

## 🚀 Funcionalidades principales
- Visualización interactiva de datos con filtros por país, año y tipo.
- Gráficos descriptivos utilizando Seaborn y Matplotlib.
- Exploración de clasificaciones y ratings por contenido.
- App embebida en contenedor Docker para facilitar su despliegue.

## 🐳 Cómo ejecutar con Docker:
### 1. Obtener la imagen desde Docker Hub
docker pull francis133/dashboard-proyecto_streaming:v1

### 2. Ejecutar el contenedor
docker run -p 8501:8501 francis133/dashboard-proyecto_streaming:v1

### 3. Abrir la app
Visita http://localhost:8501 en tu navegador para explorar el dashboard 📊

## Estructura del proyecto 📑
Proyecto_Streaming/
├── data/              # Conjuntos de datos en formato CSV y parquet
├── notebooks/         # Jupyter notebooks de limpieza de datos y análisis exploratorio 
├── scripts/           # Contiene app.py y funciones generales aplicadas a la limpieza de datos
├── requirements.txt   # Librerías necesarias
├── Dockerfile         # Imagen de Docker
└── README.md          # Este archivo

## ⚙️ Instalación manual (sin Docker)
Si prefieres correr el proyecto localmente:

```bash
# Clona este repositorio
git clone https://github.com/Crismar12/Proyecto_Streaming.git
cd Proyecto_Streaming

# Crea un entorno virtual e instala dependencias
python -m venv venv
venv\Scripts\activate   # En Windows
pip install -r requirements.txt

# Ejecuta la app
streamlit run scripts/app.py
```
## ✨ Autor
Desarrollado por Francis 🧠 Con ❤️ por la visualización de datos y la ingeniería de sistemas e informática.

