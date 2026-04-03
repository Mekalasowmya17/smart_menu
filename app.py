from flask import Flask
from routes.menu_routes import menu_bp

app = Flask(__name__)
app.register_blueprint(menu_bp)

app.run(debug=True)