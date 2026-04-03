from flask import Flask
from routes.menu_routes import menu_bp

app = Flask(__name__)
app.register_blueprint(menu_bp)

if __name__ == "__main__":
    app.run(debug=True)