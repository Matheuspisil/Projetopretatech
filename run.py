import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    if os.name == 'nt':  # Se estiver no Windows
        from waitress import serve
        serve(app, host='0.0.0.0', port=8080)
    else:  # Se estiver no Unix/Linux
        app.run(debug=True)
