from flask_app import app #Python sabe que debe empezar a buscar en __init__
from flask_app.controladores import controladorDojos

if __name__ == "__main__":
    app.run(debug=True)