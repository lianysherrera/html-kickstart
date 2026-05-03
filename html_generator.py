import os
import sys
import re
from colorama import Fore, Style, init
import questionary

IDIOMAS = {
    "español": {
        "lang": "es",
        "nav": ["Inicio", "Sobre mí", "Contacto"],
        "bienvenida": "Bienvenido a",
        "footer": "Todos los derechos reservados."
    },
    "english": {
        "lang": "en",
        "nav": ["Home", "About", "Contact"],
        "bienvenida": "Welcome to",
        "footer": "All rights reserved."
    },
    "français": {
        "lang": "fr",
        "nav": ["Accueil", "À propos", "Contact"],
        "bienvenida": "Bienvenue à",
        "footer": "Tous droits réservés."
    }
}

init(autoreset=True)

def generate_html(project_name, idioma="español", nav_custom=None):
    lang = IDIOMAS[idioma]["lang"]
    nav = nav_custom if nav_custom else IDIOMAS[idioma]["nav"]
    bienvenida = IDIOMAS[idioma]["bienvenida"]
    footer = IDIOMAS[idioma]["footer"]

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Serif+Display&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" href="favicon.ico">
</head>
<body>

    <header class="header">
        <nav class="nav">
            <a href="#" class="nav__logo">{project_name}</a>
            <ul class="nav__links">
                <li><a href="#">{nav[0]}</a></li>
                <li><a href="#">{nav[1]}</a></li>
                <li><a href="#">{nav[2]}</a></li>
            </ul>
        </nav>
    </header>

    <main class="main">
        <div class="hero">
            <span class="hero__tag">{bienvenida}</span>
            <h1 class="hero__title">{project_name}</h1>
            <p class="hero__subtitle">Empieza a construir algo increíble aquí.</p>
        </div>
    </main>

    <footer class="footer">
        <p>&copy; 2025 {project_name}. {footer}</p>
    </footer>

</body>
</html>"""

def generate_css():
    return """
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
:root {
    --color-bg: #fafaf8;
    --color-text: #1a1a1a;
    --color-muted: #888;
    --color-border: #e8e8e4;
    --font-display: 'DM Serif Display', serif;
    --font-body: 'DM Sans', sans-serif;
}
body {
    font-family: var(--font-body);
    background-color: var(--color-bg);
    color: var(--color-text);
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    font-weight: 300;
}
.header {
    padding: 1.5rem 3rem;
    border-bottom: 1px solid var(--color-border);
    background-color: var(--color-bg);
    position: sticky;
    top: 0;
    z-index: 10;
}
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1100px;
    margin: 0 auto;
}
.nav__logo {
    font-family: var(--font-display);
    font-size: 1.2rem;
    color: var(--color-text);
    text-decoration: none;
}
.nav__links {
    list-style: none;
    display: flex;
    gap: 2.5rem;
}
.nav__links li a {
    color: var(--color-muted);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 400;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    transition: color 0.2s ease;
}
.nav__links li a:hover {
    color: var(--color-text);
}
.main {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 6rem 3rem;
}
.hero {
    text-align: center;
    max-width: 600px;
}
.hero__tag {
    display: inline-block;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--color-muted);
    margin-bottom: 1.5rem;
    border: 1px solid var(--color-border);
    padding: 0.3rem 0.8rem;
    border-radius: 999px;
}
.hero__title {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 6vw, 4rem);
    color: var(--color-text);
    line-height: 1.1;
    margin-bottom: 1.5rem;
    font-weight: 400;
}
.hero__subtitle {
    font-size: 1rem;
    color: var(--color-muted);
    line-height: 1.7;
    font-weight: 300;
}
.footer {
    border-top: 1px solid var(--color-border);
    padding: 1.5rem 3rem;
    text-align: center;
    font-size: 0.8rem;
    color: var(--color-muted);
    letter-spacing: 0.03em;
}
"""

def generate_css_dark():
    return """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0d0d0d;
    color: #f0f0f0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
.header {
    background-color: #111111;
    border-bottom: 1px solid #222;
    padding: 1.2rem 2rem;
}
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nav h1 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
}
.nav ul li a {
    color: #888;
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.3s;
}
.nav ul li a:hover {
    color: #ffffff;
}
.main {
    flex: 1;
    padding: 3rem 2rem;
}
.footer {
    background-color: #111111;
    border-top: 1px solid #222;
    text-align: center;
    padding: 1.2rem;
    font-size: 0.8rem;
    color: #555;
}
"""

def generate_css_colorful():
    return """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    color: #333;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
.header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 1.2rem 2rem;
}
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nav h1 {
    font-size: 1.1rem;
    font-weight: 700;
    color: white;
    letter-spacing: 1px;
}
.nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
}
.nav ul li a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.3s;
}
.nav ul li a:hover {
    color: white;
}
.main {
    flex: 1;
    padding: 3rem 2rem;
}
.footer {
    background: linear-gradient(135deg, #667eea, #764ba2);
    text-align: center;
    padding: 1.2rem;
    font-size: 0.8rem;
    color: rgba(255,255,255,0.8);
}
"""

def create_project(project_name, tema="minimalista", readme=False, idioma="español",gitignore=False, favicon=False):

    if os.path.exists(project_name):
        print(f"{Fore.YELLOW}⚠️ La carpeta '{project_name}' ya existe.")
        respuesta = input("¿Quieres sobreescribirla? (s/n):")
        if respuesta.lower() != "s":
            print(f"{Fore.RED}🚫 Operación cancelada.")
            sys.exit(1)

    os.makedirs(f"{project_name}/css", exist_ok=True)
    os.makedirs(f"{project_name}/js", exist_ok=True)

    with open(f"{project_name}/index.html", "w", encoding="utf-8") as f:
        f.write(generate_html(project_name, idioma))
    
    if tema == "oscuro":
        css = generate_css_dark()
    elif tema == "colorido":
        css = generate_css_colorful()
    else:
        css = generate_css()

    with open(f"{project_name}/css/styles.css", "w", encoding="utf-8") as f:
        f.write(css)

    with open(f"{project_name}/js/main.js", "w", encoding="utf-8") as f:
        f.write("// javascript here\n")

    print(f"{Fore.GREEN}✅ Projecto '{project_name}' creado correctamente")
    print(f"{Fore.CYAN}📁 {project_name}/")
    print(f"   ├── index.html")
    print(f"   ├── css/styles.css")
    print(f"   └── js/main.js {Style.RESET_ALL}")

    if readme:
        with open(f"{project_name}/README.md", "w", encoding="utf-8") as f:
            f.write(f"# {project_name}\n\nDescripción de tu proyecto aquí.\n")
        print(f"{Fore.GREEN}   └── 📝 README.md{Style.RESET_ALL}")

    if gitignore:
        with open(f"{project_name}/.gitignore", "w", encoding="utf-8") as f:
            f.write("node_modules/\n.venv/\n.env\n*.pyc\n.DS_Store\nThumbs.db\n")
        print(f"{Fore.GREEN}   └── 🙈 .gitignore{Style.RESET_ALL}")

    if favicon:
        import shutil
        favicon_origen = os.path.join(os.path.dirname(__file__), "favicon.ico")
        if os.path.exists(favicon_origen):
            shutil.copy(favicon_origen, f"{project_name}/favicon.ico")
            print(f"{Fore.GREEN}   └── 🖼️ favicon.ico{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}⚠️ No se encontró favicon.ico en el repo.{Style.RESET_ALL}")

def validate_project_name(name: str) -> bool:
    """ Solo permite letras, números y guiones."""
    pattern = r'^[a-zA-Z0-9-_]+$'
    return bool(re.match(pattern, name))

def main():
    print(f"{Fore.CYAN}🚀 Bienvenido a html-kickstart!{Style.RESET_ALL}")
    print()

    name = questionary.text("📝 Nombre del proyecto:").ask()

    if not name or not validate_project_name(name):
        print(f"{Fore.RED}❌ Nombre inválido. Solo se permiten letras, números, guiones y guiones bajos.{Style.RESET_ALL}")
        sys.exit(1)

    tema = questionary.select(
        "🎨 Elige un tema:",
        choices=["minimalista", "oscuro", "colorido"]
    ).ask()

    idioma = questionary.select(
        "🌍 Elige un idioma:",
        choices=["español", "english", "français"]
    ).ask()

    readme = questionary.confirm("📄 ¿Añadir un README.md al proyecto?").ask()
    gitignore = questionary.confirm("🙈 Añadir un .gitignore?").ask()
    favicon = questionary.confirm("🖼️ Añadir un favicon?").ask()

    create_project(name, tema, readme, idioma, gitignore, favicon)

if __name__ == "__main__":
    main()