# 🚀 html-kickstart

Genera una plantilla HTML lista para usar desde cualquier terminal. HTML + CSS + JS en un solo comando.

![version](https://img.shields.io/badge/version-1.0.0-purple)
![python](https://img.shields.io/badge/python-3.8+-blue)
![license](https://img.shields.io/badge/license-MIT-green)

## ✨ Características

- 3 temas: minimalista, oscuro y colorido
- 3 idiomas: español, english y français
- Menú hamburguesa responsive incluido
- Validación del nombre del proyecto
- Comprueba si la carpeta ya existe
- Colores en la terminal
- Opciones extra: README, .gitignore y favicon

## 📦 Instalación

### Windows

```bash
git clone https://github.com/tu-usuario/html-kickstart.git
cd html-kickstart
pip install -e .
```

### Ubuntu / Linux

En Ubuntu es necesario usar un entorno virtual:

```bash
git clone https://github.com/lianysherrera/html-kickstart.git
cd html-kickstart
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

> ⚠️ Cada vez que abras una terminal nueva en Ubuntu, activa el entorno virtual primero:
> ```bash
> source ~/ruta/a/html-kickstart/venv/bin/activate
> ```

## 🖥️ Uso

```bash
html-kickstart
```

El menú interactivo te guiará paso a paso:

```
🚀 Bienvenido a html-kickstart!

📝 Nombre del proyecto: mi-proyecto
🎨 Elige un tema: minimalista / oscuro / colorido
🌍 Elige un idioma: español / english / français
📄 ¿Añadir un README.md?
🙈 ¿Añadir un .gitignore?
🖼️ ¿Añadir un favicon?
```

## 📁 Estructura generada

```
mi-proyecto/
├── index.html
├── css/
│   └── styles.css
└── js/
    └── main.js
```

## ⚙️ Opciones

```bash
html-kickstart --version  # Ver versión instalada
```

## 📄 Licencia

MIT
