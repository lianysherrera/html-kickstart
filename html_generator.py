import os
import sys
import re
from colorama import Fore, Style, init

init(autoreset=True)

def generate_html(project_name):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{project_name}</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>

    <header class="header">
        <nav class="nav">
            <h1>{project_name}</h1>
            <ul>
                <li><a href="#">{project_name}</a></li>
                <li><a href="#">{project_name}</a></li>
                <li><a href="#">{project_name}</a></li>
            </ul>
        </nav>
    </header>

    <main class="main">
        <p>Bienvenido a {project_name}</p>
    </main>

    <footer class="footer">
        <p>&copy; 2025 {project_name}</p>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>"""

def generate_css():
    return """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #fff;
    color: #333;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
.header {
    background-color: #f9f9f9;
    border-bottom: 1px solid #eee;
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
    color: #111;
}
.nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
}
.nav ul li a {
    color: #666;
    text-decoration: none;
    font-size: 0.9rem;
}
.nav ul li a:hover {
    color: #111;
}
.main {
    flex: 1;
    padding: 3rem 2rem;
}
.footer {
    background-color: #f9f9f9;
    border-top: 1px solid #eee;
    text-align: center;
    padding: 1.2rem;
    font-size: 0.8rem;
    color: #aaa;
}
"""

def create_project(project_name):

    if os.path.exists(project_name):
        print(f"{Fore.YELLOW}La carpeta '{project_name}' ya existe.")
        respuesta = input("¿Quieres sobreescribirla? (s/n):")
        if respuesta.lower() != "s":
            print(f"{Fore.RED} Operación cancelada.")
            sys.exit(1)

    os.makedirs(f"{project_name}/css", exist_ok=True)
    os.makedirs(f"{project_name}/js", exist_ok=True)

    with open(f"{project_name}/index.html", "w", encoding="utf-8") as f:
        f.write(generate_html(project_name))

    with open(f"{project_name}/css/styles.css", "w", encoding="utf-8") as f:
        f.write(generate_css())

    with open(f"{project_name}/js/main.js", "w", encoding="utf-8") as f:
        f.write("// javascript here\n")

    print(f"{Fore.GREEN} Projecto '{project_name}' creado correctamente")
    print(f"{Fore.CYAN}📁 {project_name}/")
    print(f"   ├── index.html")
    print(f"   ├── css/styles.css")
    print(f"   └── js/main.js {Style.RESET_ALL}")

def validate_project_name(name: str) -> bool:
    """ Solo permite letras, números y guiones."""
    pattern = r'^[a-zA-Z0-9-_]+$'
    return bool(re.match(pattern, name))

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED} Debes indicar el nombre del proyecto.")
        print("   Uso: html-kickstart mi-proyecto{Style.RESET_ALL}")
        sys.exit(1)

    name = sys.argv[1]

    if not validate_project_name(name):
        print(f"{Fore.RED}Nombre inválido. Solo se permiten letras, números, guiones y guiones bajos.")
    create_project(name)

if __name__ == "__main__":
    main()