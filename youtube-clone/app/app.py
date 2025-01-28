from flask import Flask

def create_app():
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuración de la aplicación (puedes agregar configuraciones aquí)
    app.config['SECRET_KEY'] = 'mi_secreto'

    # Registrar rutas o blueprints (si los tienes)
    @app.route('/')
    def home():
        return "¡Hola, mundo!"

    # Puedes agregar más configuraciones y rutas según sea necesario

    return app
