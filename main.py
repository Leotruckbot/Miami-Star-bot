from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot de búsqueda de piezas - Miami Star 🛠️"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
