from flask import Flask

app = Flask(__name__)

@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'Hola {nombre}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)