#Importa a aplicação Flask do arquivo app/__init__.py
from app import app

#iniciar um servido 
if __name__ == '__main__':
    app.run(debug=True)
